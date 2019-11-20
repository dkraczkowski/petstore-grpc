from sqlite3 import Cursor
from typing import Tuple

from .abstract_repository import AbstractRepository
from petstore.proto.petstore_pb2 import Customer


class CustomerRepository(AbstractRepository):
    def create(self, customer: Customer) -> None:
        cursor = self.execute(
            "INSERT INTO customers(first_name, last_name, email, status) VALUES(?, ?, ?, ?)",
            customer.first_name,
            customer.last_name,
            customer.email,
            customer.status
        )
        customer.id = cursor.lastrowid

    def get(self, customer_id: int) -> Customer:
        cursor = self.execute("SELECT customer_id, first_name, last_name, email, status FROM customers WHERE customer_id = ?", customer_id)
        cursor.row_factory = customer_factory
        return cursor.fetchone()


def customer_factory(cursor: Cursor, row: Tuple[int, str, str, str, int]) -> Customer:
    return Customer(row[0], row[1], row[2], row[3], row[4])
