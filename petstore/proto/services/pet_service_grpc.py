# Generated by the Protocol Buffers compiler. DO NOT EDIT!
# source: petstore/proto/services/pet_service.proto
# plugin: grpclib.plugin.main
import abc
import typing

import grpclib.const
import grpclib.client
if typing.TYPE_CHECKING:
    import grpclib.server

import petstore.proto.petstore_pb2
import petstore.proto.services.pet_service_pb2


class PetServiceBase(abc.ABC):

    @abc.abstractmethod
    async def GetPet(self, stream: 'grpclib.server.Stream[petstore.proto.services.pet_service_pb2.GetPetRequest, petstore.proto.petstore_pb2.Pet]') -> None:
        pass

    @abc.abstractmethod
    async def ListPets(self, stream: 'grpclib.server.Stream[petstore.proto.services.pet_service_pb2.ListPetRequest, petstore.proto.services.pet_service_pb2.PetList]') -> None:
        pass

    @abc.abstractmethod
    async def CreatePet(self, stream: 'grpclib.server.Stream[petstore.proto.petstore_pb2.Pet, petstore.proto.petstore_pb2.Pet]') -> None:
        pass

    @abc.abstractmethod
    async def DeletePet(self, stream: 'grpclib.server.Stream[petstore.proto.petstore_pb2.Pet, petstore.proto.petstore_pb2.Pet]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {
            '/petstore.services.PetService/GetPet': grpclib.const.Handler(
                self.GetPet,
                grpclib.const.Cardinality.UNARY_UNARY,
                petstore.proto.services.pet_service_pb2.GetPetRequest,
                petstore.proto.petstore_pb2.Pet,
            ),
            '/petstore.services.PetService/ListPets': grpclib.const.Handler(
                self.ListPets,
                grpclib.const.Cardinality.UNARY_UNARY,
                petstore.proto.services.pet_service_pb2.ListPetRequest,
                petstore.proto.services.pet_service_pb2.PetList,
            ),
            '/petstore.services.PetService/CreatePet': grpclib.const.Handler(
                self.CreatePet,
                grpclib.const.Cardinality.UNARY_UNARY,
                petstore.proto.petstore_pb2.Pet,
                petstore.proto.petstore_pb2.Pet,
            ),
            '/petstore.services.PetService/DeletePet': grpclib.const.Handler(
                self.DeletePet,
                grpclib.const.Cardinality.UNARY_UNARY,
                petstore.proto.petstore_pb2.Pet,
                petstore.proto.petstore_pb2.Pet,
            ),
        }


class PetServiceStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.GetPet = grpclib.client.UnaryUnaryMethod(
            channel,
            '/petstore.services.PetService/GetPet',
            petstore.proto.services.pet_service_pb2.GetPetRequest,
            petstore.proto.petstore_pb2.Pet,
        )
        self.ListPets = grpclib.client.UnaryUnaryMethod(
            channel,
            '/petstore.services.PetService/ListPets',
            petstore.proto.services.pet_service_pb2.ListPetRequest,
            petstore.proto.services.pet_service_pb2.PetList,
        )
        self.CreatePet = grpclib.client.UnaryUnaryMethod(
            channel,
            '/petstore.services.PetService/CreatePet',
            petstore.proto.petstore_pb2.Pet,
            petstore.proto.petstore_pb2.Pet,
        )
        self.DeletePet = grpclib.client.UnaryUnaryMethod(
            channel,
            '/petstore.services.PetService/DeletePet',
            petstore.proto.petstore_pb2.Pet,
            petstore.proto.petstore_pb2.Pet,
        )
