import asyncio

from grpclib.client import Channel

from petstore.proto.services.category_service_pb2 import GetCategoryRequest
from petstore.proto.petstore_pb2 import Category

from petstore.proto.services.category_service_grpc import CategoryServiceStub


async def main():
    channel = Channel("127.0.0.1", 8080)
    service = CategoryServiceStub(channel)
    write_request: Category = await service.CreateCategory(Category(name="test"))
    read_request: Category = await service.GetCategory(GetCategoryRequest(category_id=write_request.id))

    print(write_request, read_request)
    channel.close()


if __name__ == "__main__":
    asyncio.run(main())
