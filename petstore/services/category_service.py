from grpclib.server import Stream

from petstore.proto.petstore_pb2 import Category
from petstore.proto.services.category_service_grpc import CategoryServiceBase
from petstore.proto.services.category_service_pb2 import GetCategoryRequest
from petstore.repositories import CategoryRepository


class CategoryService(CategoryServiceBase):
    def __init__(self, repository: CategoryRepository):
        self.category_repository = repository

    async def GetCategory(self, stream: Stream[GetCategoryRequest, Category]) -> None:
        category_request = await stream.recv_message()
        await stream.send_message(self.category_repository.get(category_request.category_id))

    async def CreateCategory(self, stream: Stream[Category, Category]) -> None:
        new_category = await stream.recv_message()
        self.category_repository.create(new_category)
        await stream.send_message(new_category)

    async def DeleteCategory(self, stream: Stream[Category, Category]) -> None:
        category = await stream.recv_message()
        self.category_repository.remove(category)
        await stream.send_message(category)
