# Copyright (c) HashiCorp, Inc.
# SPDX-License-Identifier: MPL-2.0

# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proto/kv.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0eproto/kv.proto\x12\x05proto\"\x1e\n\nGetRequest\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\"#\n\x0bGetResponse\x12\x14\n\x05value\x18\x01 \x01(\x0cR\x05value\"4\n\nPutRequest\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x14\n\x05value\x18\x02 \x01(\x0cR\x05value\"\x07\n\x05\x45mpty2Z\n\x02KV\x12,\n\x03Get\x12\x11.proto.GetRequest\x1a\x12.proto.GetResponse\x12&\n\x03Put\x12\x11.proto.PutRequest\x1a\x0c.proto.EmptyB\tZ\x07./protob\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'proto.kv_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z\007./proto'
  _globals['_GETREQUEST']._serialized_start=25
  _globals['_GETREQUEST']._serialized_end=55
  _globals['_GETRESPONSE']._serialized_start=57
  _globals['_GETRESPONSE']._serialized_end=92
  _globals['_PUTREQUEST']._serialized_start=94
  _globals['_PUTREQUEST']._serialized_end=146
  _globals['_EMPTY']._serialized_start=148
  _globals['_EMPTY']._serialized_end=155
  _globals['_KV']._serialized_start=157
  _globals['_KV']._serialized_end=247
# @@protoc_insertion_point(module_scope)
