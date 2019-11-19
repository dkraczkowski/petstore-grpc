from os import path
from sqlite3 import Connection
from sqlite3 import Row
from sqlite3 import connect

import pytest

SCHEMA_PATH = path.join(path.dirname(__file__), "../petstore/schema.sql")


@pytest.fixture
def db_mock() -> Connection:
    connection = connect(":memory:")
    connection.row_factory = Row

    sql_schema = open(SCHEMA_PATH, "r").read()
    cursor = connection.cursor()
    cursor.executescript(sql_schema)

    return connection
