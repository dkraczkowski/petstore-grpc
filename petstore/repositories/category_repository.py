from sqlite3 import Cursor
from typing import Tuple

from petstore.proto.petstore_pb2 import Category
from .abstract_repository import AbstractRepository


def hydrate_category(cursor: Cursor, row: Tuple[int, str]) -> Category:
    return Category(id=row[0], name=row[1])


class CategoryRepository(AbstractRepository):
    def get(self, category_id: int) -> Category:
        cursor = self.execute(
            "SELECT category_id, name FROM categories WHERE category_id = ? LIMIT 1",
            category_id,
        )
        cursor.row_factory = hydrate_category
        return cursor.fetchone()

    def create(self, category: Category) -> None:
        cursor = self.execute("INSERT INTO categories('name') VALUES(?)", category.name)
        category.id = cursor.lastrowid

    def remove(self, category: Category) -> None:
        self.execute("DELETE FROM categories WHERE category_id = ?", category.id)
        category.id = None
