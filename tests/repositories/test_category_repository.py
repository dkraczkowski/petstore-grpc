from sqlite3 import Row

from petstore.proto.petstore_pb2 import Category
from petstore.repositories import CategoryRepository


def test_can_create_category(db_mock):
    repository = CategoryRepository(db_mock)
    category = Category(name="test category")
    repository.create(category)

    assert category.id == 1
    assert category.name == "test category"

    cursor = db_mock.cursor()
    cursor.row_factory = Row
    cursor.execute("SELECT *FROM categories WHERE category_id = ?", [category.id])
    raw_category = dict(cursor.fetchone())

    assert raw_category == {'category_id': 1, 'name': 'test category'}


def test_can_get_category(db_mock):
    repository = CategoryRepository(db_mock)
    repository.create(Category(name="blue"))
    repository.create(Category(name="red"))
    repository.create(Category(name="green"))

    category = repository.get(1)

    assert category.id == 1
    assert category.name == "blue"
