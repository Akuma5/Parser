from bs4 import BeautifulSoup
import asyncio
from aiohttp import ClientSession
import psycopg2


def parse(int_argv):
    conn = psycopg2.connect(
        host="app",
        port=5432,
        database="suppliers",
        user="usersql",
        password="folk_user1")

    cursor = conn.cursor()

    try:
        main_list = []
        cursor.execute("SELECT * FROM apartments")
        count_page = len(cursor.fetchall())

        def house_apartments_urls(number):
            res_num = count_page // 10
            url_list = []
            for i in range(res_num + 1, number + res_num + 1):
                url_list.append(f'https://www.house.kg/kupit-kvartiru?rooms=3&region=1&town=2&price_from=30'
                                f'00000&currency=1&sort_by=upped_at%20desc&page={i}')
            return url_list

        async def parse_announcement(url_page):
            async with ClientSession() as session:
                async with session.get(url_page) as response:
                    assert response.status == 200
                    soup = BeautifulSoup((await response.read()), 'lxml')
                    number = soup.find('div', class_='number')
                    price_som = soup.find('div', class_='price-som')
                    price_dollar = soup.find('div', 'price-dollar')
                    description = soup.find('div', class_='description')
                    name = soup.find('a', 'name').text
                    some_list = [url_page]
                    if description is not None:
                        some_list.append(description.find('p').text)
                    else:
                        some_list.append('описания нет')
                    some_list.append(int(''.join((price_som.text.strip())[:-3].split())))
                    some_list.append(int(''.join((price_dollar.text.strip())[1:].split())))
                    some_list.append(number.text + '\n')
                    some_list.append(name)
                    main_list.append(some_list)

        res = []

        async def main(url_page):
            tasks = []
            async with ClientSession() as session:
                for ul in url_page:
                    async with session.get(ul) as response:
                        assert response.status == 200
                        soup = BeautifulSoup((await response.read()), 'lxml')
                        links = soup.find_all('p', class_='title')
                        for i, link in enumerate(links):
                            tasks.append(asyncio.create_task(parse_announcement('https://www.house.kg' +
                                                                                link.find('a')['href'])))
            for task in tasks:
                await task

        asyncio.run(main(house_apartments_urls(int_argv)))
        try:
            for i2, v2 in enumerate(main_list):
                change = v2[1].replace("'", '"')
                count_page += 1
                cursor.execute(
                    f"INSERT INTO apartments (id, links, description, price_som, price_dollar, number, name) VALUES "
                    f"({count_page},"
                    f" '{v2[0]}',"
                    f" '{change}', {v2[2]}, {v2[3]}, '{v2[4]}', '{v2[5]}')")
        except psycopg2.errors.UniqueViolation:
            conn.rollback()
            for i2, v2 in enumerate(main_list):
                count_page += 1
                change = v2[1].replace("'", '"')
                cursor.execute(
                    f"INSERT INTO apartments (id, links, description, price_som, price_dollar, number, name) VALUES "
                    f"({count_page}, "
                    f"'{v2[0]}',"
                    f" '{change}', {v2[2]}, {v2[3]}, '{v2[4]}', {v2[5]})")

        conn.commit()
        cursor.close()
        conn.close()
        print("Готово")
        return main_list
    except psycopg2.errors.UndefinedTable:
        print("Таблица не создана")
    except IndexError:
        print("Аргумент не передан")
