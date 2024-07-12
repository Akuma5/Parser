import psycopg2
import emoji

conn = psycopg2.connect(
    host="app",
    port=5432,
    database="suppliers",
    user="usersql",
    password="folk_user1")

cursor = conn.cursor()
try:
    cursor.execute("SELECT * FROM apartments")
    all_elem = cursor.fetchall()

    max_len1 = str(max(all_elem, key=lambda x: len(str(x[0])))[0])
    max_len2 = max(all_elem, key=lambda x: len(str(x[1])))[1]
    max_len3 = max(all_elem, key=lambda x: len(str(x[2])))[2]
    max_len4 = str(max(all_elem, key=lambda x: len(str(x[3])))[3])
    max_len5 = str(max(all_elem, key=lambda x: len(str(x[4])))[4])
    max_len6 = max(all_elem, key=lambda x: len(str(x[5])))[5]
    max_len7 = max(all_elem, key=lambda x: len(str(x[6])))[6]

    change1 = len(max_len1)
    change2 = len(max_len2)
    change3 = len(max_len3)
    change4 = len(max_len4)
    change5 = len(max_len5)
    change6 = len(max_len6)
    change7 = len(max_len7)

    price_som = 'Price som'
    price_dollar = 'Price dollar'
    if len(price_som) > change4:
        change4 = len(price_som)
    if len(price_dollar) > change5:
        change5 = len(price_dollar)

    print('ID' + '  ' + ' ' * (change2 // 2) + 'Links' + ' ' * (change2 // 2 - 5) + '  ' + ' ' * (40 // 2 - 6)
          + 'Description'
          + ' ' * (40 // 2 - 5) + '   ' + 'Price som' + '  ' + 'Price dollar' + '  ' + ' ' * (
                      change6 // 2 - 3) + 'Number' +
          ' ' * (change6 // 2 - 3) + '  ' + ' ' * (change7 // 2 - 2) + 'Name')
    print('-' * change1 + '  ' + change2 * '-' + '  ' + 40 * '-'
          + '  ' + change4 * '-' + '  ' + change5 * '-' + '  ' + change6 * '-' + '  ' + change7 * '-')
    for row in all_elem:
        text = row[2].replace('\n', ' ').replace('\r', ' ')[:40]
        text_r = ''.join(char for char in text if char not in emoji.distinct_emoji_list(text))
        print('{:>2}  {}  {}  {}  {}  {}  {}'.format(row[0], row[1].strip() + (' ' * (change2 - len(row[1]))),
                                                     text_r +
                                                     (' ' * (40 - len(text_r))),
                                                     str(row[3]) + (' ' * (change4 - len(str(row[3])))),
                                                     str(row[4]) + (' ' * (change5 - len(str(row[4])))),
                                                     row[5].strip() + (' ' * (change6 - len(str(row[5].strip())))),
                                                     row[6].strip()))
    print('-' * change1 + '  ' + change2 * '-' + '  ' + 40 * '-'
          + '  ' + change4 * '-' + '  ' + change5 * '-' + '  ' + change6 * '-' + '  ' + change7 * '-')

except psycopg2.errors.UndefinedTable:
    print("Таблица не создана")
