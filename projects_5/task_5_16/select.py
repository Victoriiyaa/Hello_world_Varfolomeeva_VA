import psycopg2

try:

    connection = psycopg2.connect(
        host="localhost",          # База в контейнере, но доступна через localhost
        port="5432",               # Порт из секции ports
        user="postgres",           # POSTGRES_USER
        password="example",        # POSTGRES_PASSWORD
        database="testdb"          # POSTGRES_DB
    )

    cursor = connection.cursor()

    cursor.execute("SELECT category FROM products;")

    products = cursor.fetchall()

    for products in products:
        print(f"Категория товара: {products}")

    cursor.close()

except Exception as error:
    print(f"Ошибка при подключении: {error}")

