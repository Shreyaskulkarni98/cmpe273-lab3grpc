# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: DBreplicator.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='DBreplicator.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x12\x44\x42replicator.proto\"\'\n\x10ReplicateRequest\x12\x13\n\x0bjson_string\x18\x01 \x01(\t\"!\n\x0eReplicateReply\x12\x0f\n\x07message\x18\x01 \x01(\t2F\n\x11ReplicatorService\x12\x31\n\tReplicate\x12\x11.ReplicateRequest\x1a\x0f.ReplicateReply\"\x00\x62\x06proto3'
)




_REPLICATEREQUEST = _descriptor.Descriptor(
  name='ReplicateRequest',
  full_name='ReplicateRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='json_string', full_name='ReplicateRequest.json_string', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=22,
  serialized_end=61,
)


_REPLICATEREPLY = _descriptor.Descriptor(
  name='ReplicateReply',
  full_name='ReplicateReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='message', full_name='ReplicateReply.message', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=63,
  serialized_end=96,
)

DESCRIPTOR.message_types_by_name['ReplicateRequest'] = _REPLICATEREQUEST
DESCRIPTOR.message_types_by_name['ReplicateReply'] = _REPLICATEREPLY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ReplicateRequest = _reflection.GeneratedProtocolMessageType('ReplicateRequest', (_message.Message,), {
  'DESCRIPTOR' : _REPLICATEREQUEST,
  '__module__' : 'DBreplicator_pb2'
  # @@protoc_insertion_point(class_scope:ReplicateRequest)
  })
_sym_db.RegisterMessage(ReplicateRequest)

ReplicateReply = _reflection.GeneratedProtocolMessageType('ReplicateReply', (_message.Message,), {
  'DESCRIPTOR' : _REPLICATEREPLY,
  '__module__' : 'DBreplicator_pb2'
  # @@protoc_insertion_point(class_scope:ReplicateReply)
  })
_sym_db.RegisterMessage(ReplicateReply)



_REPLICATORSERVICE = _descriptor.ServiceDescriptor(
  name='ReplicatorService',
  full_name='ReplicatorService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=98,
  serialized_end=168,
  methods=[
  _descriptor.MethodDescriptor(
    name='Replicate',
    full_name='ReplicatorService.Replicate',
    index=0,
    containing_service=None,
    input_type=_REPLICATEREQUEST,
    output_type=_REPLICATEREPLY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_REPLICATORSERVICE)

DESCRIPTOR.services_by_name['ReplicatorService'] = _REPLICATORSERVICE

# @@protoc_insertion_point(module_scope)
