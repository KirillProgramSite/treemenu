
import psycopg2


    # Подключиться к существующей базе данных
connection = psycopg2.connect(user="postgres",
                                  # пароль, который указали при установке PostgreSQL
                                  password="kiri2207ll",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="postgres_db")

cursor = connection.cursor()
    # Выполнение SQL-запроса для вставки данных в таблицу
insert_query = """ INSERT INTO mobile (ID, MODEL, PRICE) VALUES
                                          (1, 'IPhone 12', 1000),
                                          (2, 'Google Pixel 2', 700),
                                          (3, 'Samsung Galaxy S21', 900),
                                          (4, 'Nokia', 800)"""
cursor.execute(insert_query)
connection.commit()

