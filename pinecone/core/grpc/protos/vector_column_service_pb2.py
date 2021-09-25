#
# Copyright (c) 2020-2021 Pinecone Systems Inc. All right reserved.
#

# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: vector_column_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='vector_column_service.proto',
  package='pinecone_columnar',
  syntax='proto3',
  serialized_options=b'\n\021io.pinecone.protoZ+github.com/pinecone-io/go-pinecone/pinecone',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x1bvector_column_service.proto\x12\x11pinecone_columnar\x1a\x1cgoogle/protobuf/struct.proto\"K\n\x07NdArray\x12\x0e\n\x06\x62uffer\x18\x01 \x01(\x0c\x12\r\n\x05shape\x18\x02 \x03(\r\x12\r\n\x05\x64type\x18\x03 \x01(\t\x12\x12\n\ncompressed\x18\x04 \x01(\x08\"\xbc\x01\n\rScoredResults\x12\'\n\x03ids\x18\x01 \x01(\x0b\x32\x1a.pinecone_columnar.NdArray\x12*\n\x06scores\x18\x02 \x01(\x0b\x32\x1a.pinecone_columnar.NdArray\x12(\n\x04\x64\x61ta\x18\x03 \x01(\x0b\x32\x1a.pinecone_columnar.NdArray\x12,\n\x08metadata\x18\x04 \x01(\x0b\x32\x1a.pinecone_columnar.NdArray\"\x84\x01\n\rUpsertRequest\x12\x11\n\tnamespace\x18\x01 \x01(\t\x12\x0b\n\x03ids\x18\x02 \x03(\t\x12(\n\x04\x64\x61ta\x18\x03 \x01(\x0b\x32\x1a.pinecone_columnar.NdArray\x12)\n\x08metadata\x18\x04 \x03(\x0b\x32\x17.google.protobuf.Struct\"\x10\n\x0eUpsertResponse\"C\n\rDeleteRequest\x12\x11\n\tnamespace\x18\x01 \x01(\t\x12\x0b\n\x03ids\x18\x02 \x03(\t\x12\x12\n\ndelete_all\x18\x03 \x01(\x08\"\x10\n\x0e\x44\x65leteResponse\".\n\x0c\x46\x65tchRequest\x12\x11\n\tnamespace\x18\x01 \x01(\t\x12\x0b\n\x03ids\x18\x02 \x03(\t\"\x87\x01\n\rFetchResponse\x12\x11\n\tnamespace\x18\x01 \x01(\t\x12\x0b\n\x03ids\x18\x02 \x03(\t\x12+\n\x07vectors\x18\x03 \x03(\x0b\x32\x1a.pinecone_columnar.NdArray\x12)\n\x08metadata\x18\x04 \x03(\x0b\x32\x17.google.protobuf.Struct\"\xa1\x02\n\x0cQueryRequest\x12\x11\n\tnamespace\x18\x01 \x01(\t\x12\x1b\n\x13namespace_overrides\x18\x06 \x03(\t\x12\r\n\x05top_k\x18\x02 \x01(\r\x12\x17\n\x0ftop_k_overrides\x18\x05 \x03(\r\x12\'\n\x06\x66ilter\x18\x07 \x01(\x0b\x32\x17.google.protobuf.Struct\x12\x31\n\x10\x66ilter_overrides\x18\x08 \x03(\x0b\x32\x17.google.protobuf.Struct\x12\x16\n\x0einclude_values\x18\x03 \x01(\x08\x12\x18\n\x10include_metadata\x18\t \x01(\x08\x12+\n\x07queries\x18\x04 \x01(\x0b\x32\x1a.pinecone_columnar.NdArray\"B\n\rQueryResponse\x12\x31\n\x07matches\x18\x01 \x03(\x0b\x32 .pinecone_columnar.ScoredResults\"\x1b\n\x19\x44\x65scribeIndexStatsRequest\"(\n\x10NamespaceSummary\x12\x14\n\x0cvector_count\x18\x01 \x01(\r\"\xda\x01\n\x1a\x44\x65scribeIndexStatsResponse\x12Q\n\nnamespaces\x18\x01 \x03(\x0b\x32=.pinecone_columnar.DescribeIndexStatsResponse.NamespacesEntry\x12\x11\n\tdimension\x18\x02 \x01(\r\x1aV\n\x0fNamespacesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x32\n\x05value\x18\x02 \x01(\x0b\x32#.pinecone_columnar.NamespaceSummary:\x02\x38\x01\x32\xc8\x03\n\x13VectorColumnService\x12O\n\x06Upsert\x12 .pinecone_columnar.UpsertRequest\x1a!.pinecone_columnar.UpsertResponse\"\x00\x12O\n\x06\x44\x65lete\x12 .pinecone_columnar.DeleteRequest\x1a!.pinecone_columnar.DeleteResponse\"\x00\x12L\n\x05\x46\x65tch\x12\x1f.pinecone_columnar.FetchRequest\x1a .pinecone_columnar.FetchResponse\"\x00\x12L\n\x05Query\x12\x1f.pinecone_columnar.QueryRequest\x1a .pinecone_columnar.QueryResponse\"\x00\x12s\n\x12\x44\x65scribeIndexStats\x12,.pinecone_columnar.DescribeIndexStatsRequest\x1a-.pinecone_columnar.DescribeIndexStatsResponse\"\x00\x42@\n\x11io.pinecone.protoZ+github.com/pinecone-io/go-pinecone/pineconeb\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_struct__pb2.DESCRIPTOR,])




_NDARRAY = _descriptor.Descriptor(
  name='NdArray',
  full_name='pinecone_columnar.NdArray',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='buffer', full_name='pinecone_columnar.NdArray.buffer', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='shape', full_name='pinecone_columnar.NdArray.shape', index=1,
      number=2, type=13, cpp_type=3, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='dtype', full_name='pinecone_columnar.NdArray.dtype', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='compressed', full_name='pinecone_columnar.NdArray.compressed', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=80,
  serialized_end=155,
)


_SCOREDRESULTS = _descriptor.Descriptor(
  name='ScoredResults',
  full_name='pinecone_columnar.ScoredResults',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='ids', full_name='pinecone_columnar.ScoredResults.ids', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='scores', full_name='pinecone_columnar.ScoredResults.scores', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='data', full_name='pinecone_columnar.ScoredResults.data', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='metadata', full_name='pinecone_columnar.ScoredResults.metadata', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=158,
  serialized_end=346,
)


_UPSERTREQUEST = _descriptor.Descriptor(
  name='UpsertRequest',
  full_name='pinecone_columnar.UpsertRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='namespace', full_name='pinecone_columnar.UpsertRequest.namespace', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='ids', full_name='pinecone_columnar.UpsertRequest.ids', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='data', full_name='pinecone_columnar.UpsertRequest.data', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='metadata', full_name='pinecone_columnar.UpsertRequest.metadata', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=349,
  serialized_end=481,
)


_UPSERTRESPONSE = _descriptor.Descriptor(
  name='UpsertResponse',
  full_name='pinecone_columnar.UpsertResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
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
  serialized_start=483,
  serialized_end=499,
)


_DELETEREQUEST = _descriptor.Descriptor(
  name='DeleteRequest',
  full_name='pinecone_columnar.DeleteRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='namespace', full_name='pinecone_columnar.DeleteRequest.namespace', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='ids', full_name='pinecone_columnar.DeleteRequest.ids', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='delete_all', full_name='pinecone_columnar.DeleteRequest.delete_all', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=501,
  serialized_end=568,
)


_DELETERESPONSE = _descriptor.Descriptor(
  name='DeleteResponse',
  full_name='pinecone_columnar.DeleteResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
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
  serialized_start=570,
  serialized_end=586,
)


_FETCHREQUEST = _descriptor.Descriptor(
  name='FetchRequest',
  full_name='pinecone_columnar.FetchRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='namespace', full_name='pinecone_columnar.FetchRequest.namespace', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='ids', full_name='pinecone_columnar.FetchRequest.ids', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=588,
  serialized_end=634,
)


_FETCHRESPONSE = _descriptor.Descriptor(
  name='FetchResponse',
  full_name='pinecone_columnar.FetchResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='namespace', full_name='pinecone_columnar.FetchResponse.namespace', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='ids', full_name='pinecone_columnar.FetchResponse.ids', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='vectors', full_name='pinecone_columnar.FetchResponse.vectors', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='metadata', full_name='pinecone_columnar.FetchResponse.metadata', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=637,
  serialized_end=772,
)


_QUERYREQUEST = _descriptor.Descriptor(
  name='QueryRequest',
  full_name='pinecone_columnar.QueryRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='namespace', full_name='pinecone_columnar.QueryRequest.namespace', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='namespace_overrides', full_name='pinecone_columnar.QueryRequest.namespace_overrides', index=1,
      number=6, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='top_k', full_name='pinecone_columnar.QueryRequest.top_k', index=2,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='top_k_overrides', full_name='pinecone_columnar.QueryRequest.top_k_overrides', index=3,
      number=5, type=13, cpp_type=3, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='filter', full_name='pinecone_columnar.QueryRequest.filter', index=4,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='filter_overrides', full_name='pinecone_columnar.QueryRequest.filter_overrides', index=5,
      number=8, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='include_values', full_name='pinecone_columnar.QueryRequest.include_values', index=6,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='include_metadata', full_name='pinecone_columnar.QueryRequest.include_metadata', index=7,
      number=9, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='queries', full_name='pinecone_columnar.QueryRequest.queries', index=8,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=775,
  serialized_end=1064,
)


_QUERYRESPONSE = _descriptor.Descriptor(
  name='QueryResponse',
  full_name='pinecone_columnar.QueryResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='matches', full_name='pinecone_columnar.QueryResponse.matches', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=1066,
  serialized_end=1132,
)


_DESCRIBEINDEXSTATSREQUEST = _descriptor.Descriptor(
  name='DescribeIndexStatsRequest',
  full_name='pinecone_columnar.DescribeIndexStatsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
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
  serialized_start=1134,
  serialized_end=1161,
)


_NAMESPACESUMMARY = _descriptor.Descriptor(
  name='NamespaceSummary',
  full_name='pinecone_columnar.NamespaceSummary',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='vector_count', full_name='pinecone_columnar.NamespaceSummary.vector_count', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=1163,
  serialized_end=1203,
)


_DESCRIBEINDEXSTATSRESPONSE_NAMESPACESENTRY = _descriptor.Descriptor(
  name='NamespacesEntry',
  full_name='pinecone_columnar.DescribeIndexStatsResponse.NamespacesEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='pinecone_columnar.DescribeIndexStatsResponse.NamespacesEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='pinecone_columnar.DescribeIndexStatsResponse.NamespacesEntry.value', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'8\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1338,
  serialized_end=1424,
)

_DESCRIBEINDEXSTATSRESPONSE = _descriptor.Descriptor(
  name='DescribeIndexStatsResponse',
  full_name='pinecone_columnar.DescribeIndexStatsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='namespaces', full_name='pinecone_columnar.DescribeIndexStatsResponse.namespaces', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='dimension', full_name='pinecone_columnar.DescribeIndexStatsResponse.dimension', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_DESCRIBEINDEXSTATSRESPONSE_NAMESPACESENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1206,
  serialized_end=1424,
)

_SCOREDRESULTS.fields_by_name['ids'].message_type = _NDARRAY
_SCOREDRESULTS.fields_by_name['scores'].message_type = _NDARRAY
_SCOREDRESULTS.fields_by_name['data'].message_type = _NDARRAY
_SCOREDRESULTS.fields_by_name['metadata'].message_type = _NDARRAY
_UPSERTREQUEST.fields_by_name['data'].message_type = _NDARRAY
_UPSERTREQUEST.fields_by_name['metadata'].message_type = google_dot_protobuf_dot_struct__pb2._STRUCT
_FETCHRESPONSE.fields_by_name['vectors'].message_type = _NDARRAY
_FETCHRESPONSE.fields_by_name['metadata'].message_type = google_dot_protobuf_dot_struct__pb2._STRUCT
_QUERYREQUEST.fields_by_name['filter'].message_type = google_dot_protobuf_dot_struct__pb2._STRUCT
_QUERYREQUEST.fields_by_name['filter_overrides'].message_type = google_dot_protobuf_dot_struct__pb2._STRUCT
_QUERYREQUEST.fields_by_name['queries'].message_type = _NDARRAY
_QUERYRESPONSE.fields_by_name['matches'].message_type = _SCOREDRESULTS
_DESCRIBEINDEXSTATSRESPONSE_NAMESPACESENTRY.fields_by_name['value'].message_type = _NAMESPACESUMMARY
_DESCRIBEINDEXSTATSRESPONSE_NAMESPACESENTRY.containing_type = _DESCRIBEINDEXSTATSRESPONSE
_DESCRIBEINDEXSTATSRESPONSE.fields_by_name['namespaces'].message_type = _DESCRIBEINDEXSTATSRESPONSE_NAMESPACESENTRY
DESCRIPTOR.message_types_by_name['NdArray'] = _NDARRAY
DESCRIPTOR.message_types_by_name['ScoredResults'] = _SCOREDRESULTS
DESCRIPTOR.message_types_by_name['UpsertRequest'] = _UPSERTREQUEST
DESCRIPTOR.message_types_by_name['UpsertResponse'] = _UPSERTRESPONSE
DESCRIPTOR.message_types_by_name['DeleteRequest'] = _DELETEREQUEST
DESCRIPTOR.message_types_by_name['DeleteResponse'] = _DELETERESPONSE
DESCRIPTOR.message_types_by_name['FetchRequest'] = _FETCHREQUEST
DESCRIPTOR.message_types_by_name['FetchResponse'] = _FETCHRESPONSE
DESCRIPTOR.message_types_by_name['QueryRequest'] = _QUERYREQUEST
DESCRIPTOR.message_types_by_name['QueryResponse'] = _QUERYRESPONSE
DESCRIPTOR.message_types_by_name['DescribeIndexStatsRequest'] = _DESCRIBEINDEXSTATSREQUEST
DESCRIPTOR.message_types_by_name['NamespaceSummary'] = _NAMESPACESUMMARY
DESCRIPTOR.message_types_by_name['DescribeIndexStatsResponse'] = _DESCRIBEINDEXSTATSRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

NdArray = _reflection.GeneratedProtocolMessageType('NdArray', (_message.Message,), {
  'DESCRIPTOR' : _NDARRAY,
  '__module__' : 'vector_column_service_pb2'
  # @@protoc_insertion_point(class_scope:pinecone_columnar.NdArray)
  })
_sym_db.RegisterMessage(NdArray)

ScoredResults = _reflection.GeneratedProtocolMessageType('ScoredResults', (_message.Message,), {
  'DESCRIPTOR' : _SCOREDRESULTS,
  '__module__' : 'vector_column_service_pb2'
  # @@protoc_insertion_point(class_scope:pinecone_columnar.ScoredResults)
  })
_sym_db.RegisterMessage(ScoredResults)

UpsertRequest = _reflection.GeneratedProtocolMessageType('UpsertRequest', (_message.Message,), {
  'DESCRIPTOR' : _UPSERTREQUEST,
  '__module__' : 'vector_column_service_pb2'
  # @@protoc_insertion_point(class_scope:pinecone_columnar.UpsertRequest)
  })
_sym_db.RegisterMessage(UpsertRequest)

UpsertResponse = _reflection.GeneratedProtocolMessageType('UpsertResponse', (_message.Message,), {
  'DESCRIPTOR' : _UPSERTRESPONSE,
  '__module__' : 'vector_column_service_pb2'
  # @@protoc_insertion_point(class_scope:pinecone_columnar.UpsertResponse)
  })
_sym_db.RegisterMessage(UpsertResponse)

DeleteRequest = _reflection.GeneratedProtocolMessageType('DeleteRequest', (_message.Message,), {
  'DESCRIPTOR' : _DELETEREQUEST,
  '__module__' : 'vector_column_service_pb2'
  # @@protoc_insertion_point(class_scope:pinecone_columnar.DeleteRequest)
  })
_sym_db.RegisterMessage(DeleteRequest)

DeleteResponse = _reflection.GeneratedProtocolMessageType('DeleteResponse', (_message.Message,), {
  'DESCRIPTOR' : _DELETERESPONSE,
  '__module__' : 'vector_column_service_pb2'
  # @@protoc_insertion_point(class_scope:pinecone_columnar.DeleteResponse)
  })
_sym_db.RegisterMessage(DeleteResponse)

FetchRequest = _reflection.GeneratedProtocolMessageType('FetchRequest', (_message.Message,), {
  'DESCRIPTOR' : _FETCHREQUEST,
  '__module__' : 'vector_column_service_pb2'
  # @@protoc_insertion_point(class_scope:pinecone_columnar.FetchRequest)
  })
_sym_db.RegisterMessage(FetchRequest)

FetchResponse = _reflection.GeneratedProtocolMessageType('FetchResponse', (_message.Message,), {
  'DESCRIPTOR' : _FETCHRESPONSE,
  '__module__' : 'vector_column_service_pb2'
  # @@protoc_insertion_point(class_scope:pinecone_columnar.FetchResponse)
  })
_sym_db.RegisterMessage(FetchResponse)

QueryRequest = _reflection.GeneratedProtocolMessageType('QueryRequest', (_message.Message,), {
  'DESCRIPTOR' : _QUERYREQUEST,
  '__module__' : 'vector_column_service_pb2'
  # @@protoc_insertion_point(class_scope:pinecone_columnar.QueryRequest)
  })
_sym_db.RegisterMessage(QueryRequest)

QueryResponse = _reflection.GeneratedProtocolMessageType('QueryResponse', (_message.Message,), {
  'DESCRIPTOR' : _QUERYRESPONSE,
  '__module__' : 'vector_column_service_pb2'
  # @@protoc_insertion_point(class_scope:pinecone_columnar.QueryResponse)
  })
_sym_db.RegisterMessage(QueryResponse)

DescribeIndexStatsRequest = _reflection.GeneratedProtocolMessageType('DescribeIndexStatsRequest', (_message.Message,), {
  'DESCRIPTOR' : _DESCRIBEINDEXSTATSREQUEST,
  '__module__' : 'vector_column_service_pb2'
  # @@protoc_insertion_point(class_scope:pinecone_columnar.DescribeIndexStatsRequest)
  })
_sym_db.RegisterMessage(DescribeIndexStatsRequest)

NamespaceSummary = _reflection.GeneratedProtocolMessageType('NamespaceSummary', (_message.Message,), {
  'DESCRIPTOR' : _NAMESPACESUMMARY,
  '__module__' : 'vector_column_service_pb2'
  # @@protoc_insertion_point(class_scope:pinecone_columnar.NamespaceSummary)
  })
_sym_db.RegisterMessage(NamespaceSummary)

DescribeIndexStatsResponse = _reflection.GeneratedProtocolMessageType('DescribeIndexStatsResponse', (_message.Message,), {

  'NamespacesEntry' : _reflection.GeneratedProtocolMessageType('NamespacesEntry', (_message.Message,), {
    'DESCRIPTOR' : _DESCRIBEINDEXSTATSRESPONSE_NAMESPACESENTRY,
    '__module__' : 'vector_column_service_pb2'
    # @@protoc_insertion_point(class_scope:pinecone_columnar.DescribeIndexStatsResponse.NamespacesEntry)
    })
  ,
  'DESCRIPTOR' : _DESCRIBEINDEXSTATSRESPONSE,
  '__module__' : 'vector_column_service_pb2'
  # @@protoc_insertion_point(class_scope:pinecone_columnar.DescribeIndexStatsResponse)
  })
_sym_db.RegisterMessage(DescribeIndexStatsResponse)
_sym_db.RegisterMessage(DescribeIndexStatsResponse.NamespacesEntry)


DESCRIPTOR._options = None
_DESCRIBEINDEXSTATSRESPONSE_NAMESPACESENTRY._options = None

_VECTORCOLUMNSERVICE = _descriptor.ServiceDescriptor(
  name='VectorColumnService',
  full_name='pinecone_columnar.VectorColumnService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=1427,
  serialized_end=1883,
  methods=[
  _descriptor.MethodDescriptor(
    name='Upsert',
    full_name='pinecone_columnar.VectorColumnService.Upsert',
    index=0,
    containing_service=None,
    input_type=_UPSERTREQUEST,
    output_type=_UPSERTRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Delete',
    full_name='pinecone_columnar.VectorColumnService.Delete',
    index=1,
    containing_service=None,
    input_type=_DELETEREQUEST,
    output_type=_DELETERESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Fetch',
    full_name='pinecone_columnar.VectorColumnService.Fetch',
    index=2,
    containing_service=None,
    input_type=_FETCHREQUEST,
    output_type=_FETCHRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Query',
    full_name='pinecone_columnar.VectorColumnService.Query',
    index=3,
    containing_service=None,
    input_type=_QUERYREQUEST,
    output_type=_QUERYRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='DescribeIndexStats',
    full_name='pinecone_columnar.VectorColumnService.DescribeIndexStats',
    index=4,
    containing_service=None,
    input_type=_DESCRIBEINDEXSTATSREQUEST,
    output_type=_DESCRIBEINDEXSTATSRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_VECTORCOLUMNSERVICE)

DESCRIPTOR.services_by_name['VectorColumnService'] = _VECTORCOLUMNSERVICE

# @@protoc_insertion_point(module_scope)