import psycopg2


conn = psycopg2.connect(
    host="app",
    port=5432,
    database="suppliers",
    user="usersql",
    password="folk_user1")

cursor = conn.cursor()
try:
    cursor.execute("CREATE TABLE apartments (id SERIAL PRIMARY KEY, links VARCHAR, description VARCHAR, "
                   "price_som INTEGER,"
                   " price_dollar INTEGER, number VARCHAR, name VARCHAR)")
    print('Таблица создана')
except psycopg2.errors.DuplicateTable:
    print('Таблица уже создана')

conn.commit()
cursor.close()
conn.close()
