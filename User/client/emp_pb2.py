# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: emp.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\temp.proto\"D\n\nAddRequest\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0c\n\x04\x63ity\x18\x03 \x01(\t\x12\x0e\n\x06salary\x18\x04 \x01(\x05\"\x1d\n\x0b\x41\x64\x64Response\x12\x0e\n\x06result\x18\x01 \x01(\t\"\x19\n\x0bReadRequest\x12\n\n\x02id\x18\x01 \x01(\x05\"V\n\x0cReadResponse\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0c\n\x04\x63ity\x18\x03 \x01(\t\x12\x0e\n\x06salary\x18\x04 \x01(\x05\x12\x0e\n\x06result\x18\x05 \x01(\t\"G\n\rUpdateRequest\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0c\n\x04\x63ity\x18\x03 \x01(\t\x12\x0e\n\x06salary\x18\x04 \x01(\x05\" \n\x0eUpdateResponse\x12\x0e\n\x06result\x18\x01 \x01(\t\"\x1b\n\rDeleteRequest\x12\n\n\x02id\x18\x01 \x01(\x05\" \n\x0e\x44\x65leteResponse\x12\x0e\n\x06result\x18\x01 \x01(\t\"=\n\x03\x45mp\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0c\n\x04\x63ity\x18\x03 \x01(\t\x12\x0e\n\x06salary\x18\x04 \x01(\x05\x32\xbb\x01\n\x10\x45mployeesService\x12#\n\x06\x41\x64\x64\x45mp\x12\x0b.AddRequest\x1a\x0c.AddResponse\x12&\n\x07ReadEmp\x12\x0c.ReadRequest\x1a\r.ReadResponse\x12,\n\tUpdateEmp\x12\x0e.UpdateRequest\x1a\x0f.UpdateResponse\x12,\n\tDeleteEmp\x12\x0e.DeleteRequest\x1a\x0f.DeleteResponseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'emp_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_ADDREQUEST']._serialized_start=13
  _globals['_ADDREQUEST']._serialized_end=81
  _globals['_ADDRESPONSE']._serialized_start=83
  _globals['_ADDRESPONSE']._serialized_end=112
  _globals['_READREQUEST']._serialized_start=114
  _globals['_READREQUEST']._serialized_end=139
  _globals['_READRESPONSE']._serialized_start=141
  _globals['_READRESPONSE']._serialized_end=227
  _globals['_UPDATEREQUEST']._serialized_start=229
  _globals['_UPDATEREQUEST']._serialized_end=300
  _globals['_UPDATERESPONSE']._serialized_start=302
  _globals['_UPDATERESPONSE']._serialized_end=334
  _globals['_DELETEREQUEST']._serialized_start=336
  _globals['_DELETEREQUEST']._serialized_end=363
  _globals['_DELETERESPONSE']._serialized_start=365
  _globals['_DELETERESPONSE']._serialized_end=397
  _globals['_EMP']._serialized_start=399
  _globals['_EMP']._serialized_end=460
  _globals['_EMPLOYEESSERVICE']._serialized_start=463
  _globals['_EMPLOYEESSERVICE']._serialized_end=650
# @@protoc_insertion_point(module_scope)
