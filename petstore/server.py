import asyncio
from os import path
import sqlite3

from grpclib.server import Server
from grpclib.utils import graceful_exit

from petstore import repositories
from petstore import services

DB_PATH = path.join(path.dirname(__file__), "petstore.db")
SCHEMA_PATH = path.join(path.dirname(__file__), "schema.sql")
HOST = "127.0.0.1"
PORT = 8080


async def main():
    if not path.isfile(DB_PATH):
        create_database(DB_PATH)

    db_connection = sqlite3.connect(DB_PATH)
    category_service = services.CategoryService(repositories.CategoryRepository(db_connection))

    server = Server([category_service])
    with graceful_exit([server]):
        await server.start(HOST, PORT)
        print(f"Serving on {HOST}:{PORT}")
        await server.wait_closed()
        db_connection.commit()
        db_connection.close()


def create_database(path: str):
    db = sqlite3.connect(path)
    cursor = db.cursor()
    with open(SCHEMA_PATH, "r") as sql_schema_file:
        sql_schema = sql_schema_file.read()
        cursor.executescript(sql_schema)
        db.commit()
        db.close()


if __name__ == "__main__":
    asyncio.run(main())
