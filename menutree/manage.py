
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

    # Подключение к существующей базе данных
connection = psycopg2.connect(user="postgres",
                            password="1111",
                            host="127.0.0.1",
                            port="5432")
connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
cursor = connection.cursor()
sql_create_database = 'create database qwe_db'
cursor.execute(sql_create_database)
