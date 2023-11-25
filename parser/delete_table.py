import psycopg2


conn = psycopg2.connect(
    host="app",
    port=5432,
    database="suppliers",
    user="usersql",
    password="folk_user1")

cursor = conn.cursor()
try:
    cursor.execute('DROP TABLE apartments')
    print('Удаление завершено ')
except psycopg2.errors.UndefinedTable:
    print('Таблица apartments уже удалена')

conn.commit()
cursor.close()
conn.close()
