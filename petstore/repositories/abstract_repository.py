from sqlite3 import Connection, Cursor
from abc import ABC


class AbstractRepository(ABC):
    def __init__(self, connection: Connection):
        self.connection = connection

    def execute(self, statement, *args) -> Cursor:
        cursor = self.connection.cursor()
        cursor.execute(statement, args)

        return cursor
