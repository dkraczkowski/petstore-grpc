# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: petstore/proto/petstore.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='petstore/proto/petstore.proto',
  package='petstore',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x1dpetstore/proto/petstore.proto\x12\x08petstore\x1a\x1fgoogle/protobuf/timestamp.proto\".\n\x05Photo\x12\n\n\x02id\x18\x01 \x01(\r\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0b\n\x03url\x18\x03 \x01(\t\"$\n\x08\x43\x61tegory\x12\n\n\x02id\x18\x01 \x01(\r\x12\x0c\n\x04name\x18\x02 \x01(\t\"\xce\x01\n\x03Pet\x12\n\n\x02id\x18\x01 \x01(\r\x12\x0c\n\x04name\x18\x02 \x01(\t\x12$\n\x08\x63\x61tegory\x18\x03 \x01(\x0b\x32\x12.petstore.Category\x12\x1f\n\x06photos\x18\x04 \x03(\x0b\x32\x0f.petstore.Photo\x12\'\n\x06status\x18\x05 \x01(\x0e\x32\x17.petstore.Pet.PetStatus\"=\n\tPetStatus\x12\r\n\tAVAILABLE\x10\x00\x12\x0b\n\x07PENDING\x10\x01\x12\n\n\x06\x42OOKED\x10\x02\x12\x08\n\x04SOLD\x10\x03\"\xa9\x01\n\x08\x43ustomer\x12\n\n\x02id\x18\x01 \x01(\r\x12\x12\n\nfirst_name\x18\x02 \x01(\t\x12\x11\n\tlast_name\x18\x03 \x01(\t\x12\r\n\x05\x65mail\x18\x04 \x01(\t\x12\x30\n\x06status\x18\x05 \x01(\x0e\x32 .petstore.Customer.AccountStatus\")\n\rAccountStatus\x12\n\n\x06\x41\x43TIVE\x10\x00\x12\x0c\n\x08INACTIVE\x10\x01\"\xe9\x01\n\x05Order\x12\n\n\x02id\x18\x01 \x01(\r\x12$\n\x08\x63ustomer\x18\x02 \x01(\x0b\x32\x12.petstore.Customer\x12\x1a\n\x03pet\x18\x03 \x01(\x0b\x32\r.petstore.Pet\x12-\n\tship_date\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12+\n\x06status\x18\x05 \x01(\x0e\x32\x1b.petstore.Order.OrderStatus\"6\n\x0bOrderStatus\x12\n\n\x06PLACED\x10\x00\x12\x0c\n\x08\x41PPROVED\x10\x01\x12\r\n\tDELIVERED\x10\x02\x62\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,])



_PET_PETSTATUS = _descriptor.EnumDescriptor(
  name='PetStatus',
  full_name='petstore.Pet.PetStatus',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='AVAILABLE', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PENDING', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BOOKED', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SOLD', index=3, number=3,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=308,
  serialized_end=369,
)
_sym_db.RegisterEnumDescriptor(_PET_PETSTATUS)

_CUSTOMER_ACCOUNTSTATUS = _descriptor.EnumDescriptor(
  name='AccountStatus',
  full_name='petstore.Customer.AccountStatus',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='ACTIVE', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INACTIVE', index=1, number=1,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=500,
  serialized_end=541,
)
_sym_db.RegisterEnumDescriptor(_CUSTOMER_ACCOUNTSTATUS)

_ORDER_ORDERSTATUS = _descriptor.EnumDescriptor(
  name='OrderStatus',
  full_name='petstore.Order.OrderStatus',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='PLACED', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='APPROVED', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DELIVERED', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=723,
  serialized_end=777,
)
_sym_db.RegisterEnumDescriptor(_ORDER_ORDERSTATUS)


_PHOTO = _descriptor.Descriptor(
  name='Photo',
  full_name='petstore.Photo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='petstore.Photo.id', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='petstore.Photo.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='url', full_name='petstore.Photo.url', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=76,
  serialized_end=122,
)


_CATEGORY = _descriptor.Descriptor(
  name='Category',
  full_name='petstore.Category',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='petstore.Category.id', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='petstore.Category.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=124,
  serialized_end=160,
)


_PET = _descriptor.Descriptor(
  name='Pet',
  full_name='petstore.Pet',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='petstore.Pet.id', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='petstore.Pet.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='category', full_name='petstore.Pet.category', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='photos', full_name='petstore.Pet.photos', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='status', full_name='petstore.Pet.status', index=4,
      number=5, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _PET_PETSTATUS,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=163,
  serialized_end=369,
)


_CUSTOMER = _descriptor.Descriptor(
  name='Customer',
  full_name='petstore.Customer',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='petstore.Customer.id', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='first_name', full_name='petstore.Customer.first_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='last_name', full_name='petstore.Customer.last_name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='email', full_name='petstore.Customer.email', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='status', full_name='petstore.Customer.status', index=4,
      number=5, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _CUSTOMER_ACCOUNTSTATUS,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=372,
  serialized_end=541,
)


_ORDER = _descriptor.Descriptor(
  name='Order',
  full_name='petstore.Order',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='petstore.Order.id', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='customer', full_name='petstore.Order.customer', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pet', full_name='petstore.Order.pet', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ship_date', full_name='petstore.Order.ship_date', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='status', full_name='petstore.Order.status', index=4,
      number=5, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _ORDER_ORDERSTATUS,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=544,
  serialized_end=777,
)

_PET.fields_by_name['category'].message_type = _CATEGORY
_PET.fields_by_name['photos'].message_type = _PHOTO
_PET.fields_by_name['status'].enum_type = _PET_PETSTATUS
_PET_PETSTATUS.containing_type = _PET
_CUSTOMER.fields_by_name['status'].enum_type = _CUSTOMER_ACCOUNTSTATUS
_CUSTOMER_ACCOUNTSTATUS.containing_type = _CUSTOMER
_ORDER.fields_by_name['customer'].message_type = _CUSTOMER
_ORDER.fields_by_name['pet'].message_type = _PET
_ORDER.fields_by_name['ship_date'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_ORDER.fields_by_name['status'].enum_type = _ORDER_ORDERSTATUS
_ORDER_ORDERSTATUS.containing_type = _ORDER
DESCRIPTOR.message_types_by_name['Photo'] = _PHOTO
DESCRIPTOR.message_types_by_name['Category'] = _CATEGORY
DESCRIPTOR.message_types_by_name['Pet'] = _PET
DESCRIPTOR.message_types_by_name['Customer'] = _CUSTOMER
DESCRIPTOR.message_types_by_name['Order'] = _ORDER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Photo = _reflection.GeneratedProtocolMessageType('Photo', (_message.Message,), {
  'DESCRIPTOR' : _PHOTO,
  '__module__' : 'petstore.proto.petstore_pb2'
  # @@protoc_insertion_point(class_scope:petstore.Photo)
  })
_sym_db.RegisterMessage(Photo)

Category = _reflection.GeneratedProtocolMessageType('Category', (_message.Message,), {
  'DESCRIPTOR' : _CATEGORY,
  '__module__' : 'petstore.proto.petstore_pb2'
  # @@protoc_insertion_point(class_scope:petstore.Category)
  })
_sym_db.RegisterMessage(Category)

Pet = _reflection.GeneratedProtocolMessageType('Pet', (_message.Message,), {
  'DESCRIPTOR' : _PET,
  '__module__' : 'petstore.proto.petstore_pb2'
  # @@protoc_insertion_point(class_scope:petstore.Pet)
  })
_sym_db.RegisterMessage(Pet)

Customer = _reflection.GeneratedProtocolMessageType('Customer', (_message.Message,), {
  'DESCRIPTOR' : _CUSTOMER,
  '__module__' : 'petstore.proto.petstore_pb2'
  # @@protoc_insertion_point(class_scope:petstore.Customer)
  })
_sym_db.RegisterMessage(Customer)

Order = _reflection.GeneratedProtocolMessageType('Order', (_message.Message,), {
  'DESCRIPTOR' : _ORDER,
  '__module__' : 'petstore.proto.petstore_pb2'
  # @@protoc_insertion_point(class_scope:petstore.Order)
  })
_sym_db.RegisterMessage(Order)


# @@protoc_insertion_point(module_scope)