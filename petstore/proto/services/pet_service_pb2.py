# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: petstore/proto/services/pet_service.proto

import sys

_b = sys.version_info[0] < 3 and (lambda x: x) or (lambda x: x.encode("latin1"))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from petstore.proto import petstore_pb2 as petstore_dot_proto_dot_petstore__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
    name="petstore/proto/services/pet_service.proto",
    package="petstore.services",
    syntax="proto3",
    serialized_options=None,
    serialized_pb=_b(
        '\n)petstore/proto/services/pet_service.proto\x12\x11petstore.services\x1a\x1dpetstore/proto/petstore.proto"\x1f\n\rGetPetRequest\x12\x0e\n\x06pet_id\x18\x01 \x01(\r".\n\x10\x43reatePetRequest\x12\x1a\n\x03pet\x18\x01 \x01(\x0b\x32\r.petstore.Pet";\n\x07PetList\x12\x13\n\x0btotal_items\x18\x01 \x01(\r\x12\x1b\n\x04pets\x18\x02 \x03(\x0b\x32\r.petstore.Pet"6\n\x0eListPetRequest\x12\x16\n\x0eitems_per_page\x18\x01 \x01(\r\x12\x0c\n\x04page\x18\x02 \x01(\r2\xe8\x01\n\nPetService\x12\x39\n\x06GetPet\x12 .petstore.services.GetPetRequest\x1a\r.petstore.Pet\x12I\n\x08ListPets\x12!.petstore.services.ListPetRequest\x1a\x1a.petstore.services.PetList\x12)\n\tCreatePet\x12\r.petstore.Pet\x1a\r.petstore.Pet\x12)\n\tDeletePet\x12\r.petstore.Pet\x1a\r.petstore.Petb\x06proto3'
    ),
    dependencies=[petstore_dot_proto_dot_petstore__pb2.DESCRIPTOR],
)


_GETPETREQUEST = _descriptor.Descriptor(
    name="GetPetRequest",
    full_name="petstore.services.GetPetRequest",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="pet_id",
            full_name="petstore.services.GetPetRequest.pet_id",
            index=0,
            number=1,
            type=13,
            cpp_type=3,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        )
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=95,
    serialized_end=126,
)


_CREATEPETREQUEST = _descriptor.Descriptor(
    name="CreatePetRequest",
    full_name="petstore.services.CreatePetRequest",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="pet",
            full_name="petstore.services.CreatePetRequest.pet",
            index=0,
            number=1,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        )
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=128,
    serialized_end=174,
)


_PETLIST = _descriptor.Descriptor(
    name="PetList",
    full_name="petstore.services.PetList",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="total_items",
            full_name="petstore.services.PetList.total_items",
            index=0,
            number=1,
            type=13,
            cpp_type=3,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="pets",
            full_name="petstore.services.PetList.pets",
            index=1,
            number=2,
            type=11,
            cpp_type=10,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=176,
    serialized_end=235,
)


_LISTPETREQUEST = _descriptor.Descriptor(
    name="ListPetRequest",
    full_name="petstore.services.ListPetRequest",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="items_per_page",
            full_name="petstore.services.ListPetRequest.items_per_page",
            index=0,
            number=1,
            type=13,
            cpp_type=3,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="page",
            full_name="petstore.services.ListPetRequest.page",
            index=1,
            number=2,
            type=13,
            cpp_type=3,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=237,
    serialized_end=291,
)

_CREATEPETREQUEST.fields_by_name[
    "pet"
].message_type = petstore_dot_proto_dot_petstore__pb2._PET
_PETLIST.fields_by_name["pets"].message_type = petstore_dot_proto_dot_petstore__pb2._PET
DESCRIPTOR.message_types_by_name["GetPetRequest"] = _GETPETREQUEST
DESCRIPTOR.message_types_by_name["CreatePetRequest"] = _CREATEPETREQUEST
DESCRIPTOR.message_types_by_name["PetList"] = _PETLIST
DESCRIPTOR.message_types_by_name["ListPetRequest"] = _LISTPETREQUEST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetPetRequest = _reflection.GeneratedProtocolMessageType(
    "GetPetRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _GETPETREQUEST,
        "__module__": "petstore.proto.services.pet_service_pb2"
        # @@protoc_insertion_point(class_scope:petstore.services.GetPetRequest)
    },
)
_sym_db.RegisterMessage(GetPetRequest)

CreatePetRequest = _reflection.GeneratedProtocolMessageType(
    "CreatePetRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _CREATEPETREQUEST,
        "__module__": "petstore.proto.services.pet_service_pb2"
        # @@protoc_insertion_point(class_scope:petstore.services.CreatePetRequest)
    },
)
_sym_db.RegisterMessage(CreatePetRequest)

PetList = _reflection.GeneratedProtocolMessageType(
    "PetList",
    (_message.Message,),
    {
        "DESCRIPTOR": _PETLIST,
        "__module__": "petstore.proto.services.pet_service_pb2"
        # @@protoc_insertion_point(class_scope:petstore.services.PetList)
    },
)
_sym_db.RegisterMessage(PetList)

ListPetRequest = _reflection.GeneratedProtocolMessageType(
    "ListPetRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _LISTPETREQUEST,
        "__module__": "petstore.proto.services.pet_service_pb2"
        # @@protoc_insertion_point(class_scope:petstore.services.ListPetRequest)
    },
)
_sym_db.RegisterMessage(ListPetRequest)


_PETSERVICE = _descriptor.ServiceDescriptor(
    name="PetService",
    full_name="petstore.services.PetService",
    file=DESCRIPTOR,
    index=0,
    serialized_options=None,
    serialized_start=294,
    serialized_end=526,
    methods=[
        _descriptor.MethodDescriptor(
            name="GetPet",
            full_name="petstore.services.PetService.GetPet",
            index=0,
            containing_service=None,
            input_type=_GETPETREQUEST,
            output_type=petstore_dot_proto_dot_petstore__pb2._PET,
            serialized_options=None,
        ),
        _descriptor.MethodDescriptor(
            name="ListPets",
            full_name="petstore.services.PetService.ListPets",
            index=1,
            containing_service=None,
            input_type=_LISTPETREQUEST,
            output_type=_PETLIST,
            serialized_options=None,
        ),
        _descriptor.MethodDescriptor(
            name="CreatePet",
            full_name="petstore.services.PetService.CreatePet",
            index=2,
            containing_service=None,
            input_type=petstore_dot_proto_dot_petstore__pb2._PET,
            output_type=petstore_dot_proto_dot_petstore__pb2._PET,
            serialized_options=None,
        ),
        _descriptor.MethodDescriptor(
            name="DeletePet",
            full_name="petstore.services.PetService.DeletePet",
            index=3,
            containing_service=None,
            input_type=petstore_dot_proto_dot_petstore__pb2._PET,
            output_type=petstore_dot_proto_dot_petstore__pb2._PET,
            serialized_options=None,
        ),
    ],
)
_sym_db.RegisterServiceDescriptor(_PETSERVICE)

DESCRIPTOR.services_by_name["PetService"] = _PETSERVICE

# @@protoc_insertion_point(module_scope)
