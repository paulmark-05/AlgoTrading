import sqlite3


class Database:

    DB_FILE = "storage/trading.db"

    @classmethod
    def connect(cls):

        return sqlite3.connect(
            cls.DB_FILE
        )