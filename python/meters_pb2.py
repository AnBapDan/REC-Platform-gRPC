# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: meters.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import transactions_pb2 as transactions__pb2
try:
  market__pb2 = transactions__pb2.market__pb2
except AttributeError:
  market__pb2 = transactions__pb2.market_pb2

from transactions_pb2 import *

DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0cmeters.proto\x12\x05proto\x1a\x12transactions.proto\"\x94\x01\n\nMeterEntry\x12\x10\n\x08\x64\x65viceId\x18\x01 \x01(\t\x12\x14\n\x0c\x61\x63tiveImport\x18\x02 \x01(\x05\x12\x14\n\x0c\x61\x63tiveExport\x18\x03 \x01(\x05\x12\x19\n\x11reactiveInductive\x18\x04 \x01(\x05\x12\x1a\n\x12reactiveCapacitive\x18\x05 \x01(\x05\x12\x11\n\ttimestamp\x18\x06 \x01(\t\"~\n\rMeterResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12.\n\x08payments\x18\x02 \x01(\x0b\x32\x17.proto.PaymentsResponseH\x00\x88\x01\x01\x12\x14\n\x07message\x18\x03 \x01(\tH\x01\x88\x01\x01\x42\x0b\n\t_paymentsB\n\n\x08_message\"\x99\x01\n\x0bQueryMeters\x12\x1a\n\rstartInterval\x18\x01 \x01(\tH\x00\x88\x01\x01\x12\x15\n\x08\x64\x65viceId\x18\x02 \x01(\tH\x01\x88\x01\x01\x12\x11\n\x04skip\x18\x03 \x01(\x05H\x02\x88\x01\x01\x12\x12\n\x05limit\x18\x04 \x01(\x05H\x03\x88\x01\x01\x42\x10\n\x0e_startIntervalB\x0b\n\t_deviceIdB\x07\n\x05_skipB\x08\n\x06_limit\"z\n\rQueryResponse\x12+\n\x07\x65ntries\x18\x01 \x03(\x0b\x32\x1a.proto.MeasurementResponse\x12\x13\n\x06status\x18\x02 \x01(\x05H\x00\x88\x01\x01\x12\x12\n\x05\x65rror\x18\x03 \x01(\tH\x01\x88\x01\x01\x42\t\n\x07_statusB\x08\n\x06_error\"S\n\x13MeasurementResponse\x12\x10\n\x08\x44\x65viceId\x18\x01 \x01(\t\x12\r\n\x05\x46ield\x18\x02 \x01(\t\x12\r\n\x05Value\x18\x03 \x01(\t\x12\x0c\n\x04\x44\x61te\x18\x04 \x01(\t2\x8b\x01\n\rMetersService\x12\x39\n\x0e\x41\x64\x64Measurement\x12\x11.proto.MeterEntry\x1a\x14.proto.MeterResponse\x12?\n\x13RetrieveMeasurement\x12\x12.proto.QueryMeters\x1a\x14.proto.QueryResponseP\x00\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'meters_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _METERENTRY._serialized_start=44
  _METERENTRY._serialized_end=192
  _METERRESPONSE._serialized_start=194
  _METERRESPONSE._serialized_end=320
  _QUERYMETERS._serialized_start=323
  _QUERYMETERS._serialized_end=476
  _QUERYRESPONSE._serialized_start=478
  _QUERYRESPONSE._serialized_end=600
  _MEASUREMENTRESPONSE._serialized_start=602
  _MEASUREMENTRESPONSE._serialized_end=685
  _METERSSERVICE._serialized_start=688
  _METERSSERVICE._serialized_end=827
# @@protoc_insertion_point(module_scope)
