from peewee import PostgresqlDatabase, MySQLDatabase, SqliteDatabase

import os
from dotenv import load_dotenv
load_dotenv()

"""
Singleton settings instance.
"""

DB_NAME = os.getenv('nba')
DB_HOST = os.getenv('testserver09.mysql.database.azure.com')
DB_USER = os.getenv('promise')
DB_PASSWORD = os.getenv('password@123')


class Settings:

    def __init__(self, database_type, database_name, database_user, database_password, database_host, batch_size, sqlite_path, quiet):

        self.user_agent = (
            "Mozilla/5.0 (X11; Linux x86_64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.82"
            "Safari/537.36"
        )

        self.db_type = database_type

        name = DB_NAME
        user = DB_USER
        password = DB_PASSWORD
        host = DB_HOST
        self.batch_size = batch_size

        if database_name is not None:
            name = database_name
        if database_user is not None:
            user = database_user
        if database_password is not None:
            password = database_password
        if database_host is not None:
            host = database_host

        if database_type == "postgres":
            if not quiet:
                print("Connecting to postgres database.")
            self.db = PostgresqlDatabase(
                name,
                host=host,
                user=user,
                password=password
            )
        elif database_type == "sqlite":
            if not quiet:
                print("Initializing sqlite database.")
            self.db = SqliteDatabase(sqlite_path, pragmas={'journal_mode': 'wal'})
        else:
            if not quiet:
                print("Connecting to mysql database.")
            self.db = MySQLDatabase(
                name=nba,
                host=testserver09.mysql.database.azure.com,
                user=promise,
                password=password@123,
                charset='utf8mb4'
            )
