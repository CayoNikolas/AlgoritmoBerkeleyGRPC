# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proto.proto
# Protobuf Python Version: 4.25.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0bproto.proto\x12\x06\x63locks\"\x1f\n\x0fTimeDiffRequest\x12\x0c\n\x04time\x18\x01 \x01(\x05\" \n\x10TimeDiffResponse\x12\x0c\n\x04\x64iff\x18\x01 \x01(\x05\"!\n\x10TimeAjustRequest\x12\r\n\x05\x61just\x18\x01 \x01(\x05\"#\n\x11TimeAjustResponse\x12\x0e\n\x06status\x18\x01 \x01(\x08\x32\x9d\x01\n\x0c\x43locksServer\x12\x44\n\x0fRequestTimeDiff\x12\x17.clocks.TimeDiffRequest\x1a\x18.clocks.TimeDiffResponse\x12G\n\x10RequestTimeAjust\x12\x18.clocks.TimeAjustRequest\x1a\x19.clocks.TimeAjustResponseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'proto_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_TIMEDIFFREQUEST']._serialized_start=23
  _globals['_TIMEDIFFREQUEST']._serialized_end=54
  _globals['_TIMEDIFFRESPONSE']._serialized_start=56
  _globals['_TIMEDIFFRESPONSE']._serialized_end=88
  _globals['_TIMEAJUSTREQUEST']._serialized_start=90
  _globals['_TIMEAJUSTREQUEST']._serialized_end=123
  _globals['_TIMEAJUSTRESPONSE']._serialized_start=125
  _globals['_TIMEAJUSTRESPONSE']._serialized_end=160
  _globals['_CLOCKSSERVER']._serialized_start=163
  _globals['_CLOCKSSERVER']._serialized_end=320
# @@protoc_insertion_point(module_scope)
