from abc import ABC
from sqlite3 import Connection
from sqlite3 import Cursor


class AbstractRepository(ABC):
    def __init__(self, connection: Connection):
        self.connection = connection

    def execute(self, statement, *args) -> Cursor:
        cursor = self.connection.cursor()
        cursor.execute(statement, args)

        return cursor
