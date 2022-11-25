# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: app/proxyman/command/command.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from xray_api.proto.common.protocol import user_pb2 as common_dot_protocol_dot_user__pb2
from xray_api.proto.common.serial import typed_message_pb2 as common_dot_serial_dot_typed__message__pb2
from xray_api.proto.core import config_pb2 as core_dot_config__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\"app/proxyman/command/command.proto\x12\x19xray.app.proxyman.command\x1a\x1a\x63ommon/protocol/user.proto\x1a!common/serial/typed_message.proto\x1a\x11\x63ore/config.proto\"<\n\x10\x41\x64\x64UserOperation\x12(\n\x04user\x18\x01 \x01(\x0b\x32\x1a.xray.common.protocol.User\"$\n\x13RemoveUserOperation\x12\r\n\x05\x65mail\x18\x01 \x01(\t\"E\n\x11\x41\x64\x64InboundRequest\x12\x30\n\x07inbound\x18\x01 \x01(\x0b\x32\x1f.xray.core.InboundHandlerConfig\"\x14\n\x12\x41\x64\x64InboundResponse\"#\n\x14RemoveInboundRequest\x12\x0b\n\x03tag\x18\x01 \x01(\t\"\x17\n\x15RemoveInboundResponse\"W\n\x13\x41lterInboundRequest\x12\x0b\n\x03tag\x18\x01 \x01(\t\x12\x33\n\toperation\x18\x02 \x01(\x0b\x32 .xray.common.serial.TypedMessage\"\x16\n\x14\x41lterInboundResponse\"H\n\x12\x41\x64\x64OutboundRequest\x12\x32\n\x08outbound\x18\x01 \x01(\x0b\x32 .xray.core.OutboundHandlerConfig\"\x15\n\x13\x41\x64\x64OutboundResponse\"$\n\x15RemoveOutboundRequest\x12\x0b\n\x03tag\x18\x01 \x01(\t\"\x18\n\x16RemoveOutboundResponse\"X\n\x14\x41lterOutboundRequest\x12\x0b\n\x03tag\x18\x01 \x01(\t\x12\x33\n\toperation\x18\x02 \x01(\x0b\x32 .xray.common.serial.TypedMessage\"\x17\n\x15\x41lterOutboundResponse\"\x08\n\x06\x43onfig2\xc5\x05\n\x0eHandlerService\x12k\n\nAddInbound\x12,.xray.app.proxyman.command.AddInboundRequest\x1a-.xray.app.proxyman.command.AddInboundResponse\"\x00\x12t\n\rRemoveInbound\x12/.xray.app.proxyman.command.RemoveInboundRequest\x1a\x30.xray.app.proxyman.command.RemoveInboundResponse\"\x00\x12q\n\x0c\x41lterInbound\x12..xray.app.proxyman.command.AlterInboundRequest\x1a/.xray.app.proxyman.command.AlterInboundResponse\"\x00\x12n\n\x0b\x41\x64\x64Outbound\x12-.xray.app.proxyman.command.AddOutboundRequest\x1a..xray.app.proxyman.command.AddOutboundResponse\"\x00\x12w\n\x0eRemoveOutbound\x12\x30.xray.app.proxyman.command.RemoveOutboundRequest\x1a\x31.xray.app.proxyman.command.RemoveOutboundResponse\"\x00\x12t\n\rAlterOutbound\x12/.xray.app.proxyman.command.AlterOutboundRequest\x1a\x30.xray.app.proxyman.command.AlterOutboundResponse\"\x00\x42m\n\x1d\x63om.xray.app.proxyman.commandP\x01Z.github.com/xtls/xray-core/app/proxyman/command\xaa\x02\x19Xray.App.Proxyman.Commandb\x06proto3')



_ADDUSEROPERATION = DESCRIPTOR.message_types_by_name['AddUserOperation']
_REMOVEUSEROPERATION = DESCRIPTOR.message_types_by_name['RemoveUserOperation']
_ADDINBOUNDREQUEST = DESCRIPTOR.message_types_by_name['AddInboundRequest']
_ADDINBOUNDRESPONSE = DESCRIPTOR.message_types_by_name['AddInboundResponse']
_REMOVEINBOUNDREQUEST = DESCRIPTOR.message_types_by_name['RemoveInboundRequest']
_REMOVEINBOUNDRESPONSE = DESCRIPTOR.message_types_by_name['RemoveInboundResponse']
_ALTERINBOUNDREQUEST = DESCRIPTOR.message_types_by_name['AlterInboundRequest']
_ALTERINBOUNDRESPONSE = DESCRIPTOR.message_types_by_name['AlterInboundResponse']
_ADDOUTBOUNDREQUEST = DESCRIPTOR.message_types_by_name['AddOutboundRequest']
_ADDOUTBOUNDRESPONSE = DESCRIPTOR.message_types_by_name['AddOutboundResponse']
_REMOVEOUTBOUNDREQUEST = DESCRIPTOR.message_types_by_name['RemoveOutboundRequest']
_REMOVEOUTBOUNDRESPONSE = DESCRIPTOR.message_types_by_name['RemoveOutboundResponse']
_ALTEROUTBOUNDREQUEST = DESCRIPTOR.message_types_by_name['AlterOutboundRequest']
_ALTEROUTBOUNDRESPONSE = DESCRIPTOR.message_types_by_name['AlterOutboundResponse']
_CONFIG = DESCRIPTOR.message_types_by_name['Config']
AddUserOperation = _reflection.GeneratedProtocolMessageType('AddUserOperation', (_message.Message,), {
  'DESCRIPTOR' : _ADDUSEROPERATION,
  '__module__' : 'app.proxyman.command.command_pb2'
  # @@protoc_insertion_point(class_scope:xray.app.proxyman.command.AddUserOperation)
  })
_sym_db.RegisterMessage(AddUserOperation)

RemoveUserOperation = _reflection.GeneratedProtocolMessageType('RemoveUserOperation', (_message.Message,), {
  'DESCRIPTOR' : _REMOVEUSEROPERATION,
  '__module__' : 'app.proxyman.command.command_pb2'
  # @@protoc_insertion_point(class_scope:xray.app.proxyman.command.RemoveUserOperation)
  })
_sym_db.RegisterMessage(RemoveUserOperation)

AddInboundRequest = _reflection.GeneratedProtocolMessageType('AddInboundRequest', (_message.Message,), {
  'DESCRIPTOR' : _ADDINBOUNDREQUEST,
  '__module__' : 'app.proxyman.command.command_pb2'
  # @@protoc_insertion_point(class_scope:xray.app.proxyman.command.AddInboundRequest)
  })
_sym_db.RegisterMessage(AddInboundRequest)

AddInboundResponse = _reflection.GeneratedProtocolMessageType('AddInboundResponse', (_message.Message,), {
  'DESCRIPTOR' : _ADDINBOUNDRESPONSE,
  '__module__' : 'app.proxyman.command.command_pb2'
  # @@protoc_insertion_point(class_scope:xray.app.proxyman.command.AddInboundResponse)
  })
_sym_db.RegisterMessage(AddInboundResponse)

RemoveInboundRequest = _reflection.GeneratedProtocolMessageType('RemoveInboundRequest', (_message.Message,), {
  'DESCRIPTOR' : _REMOVEINBOUNDREQUEST,
  '__module__' : 'app.proxyman.command.command_pb2'
  # @@protoc_insertion_point(class_scope:xray.app.proxyman.command.RemoveInboundRequest)
  })
_sym_db.RegisterMessage(RemoveInboundRequest)

RemoveInboundResponse = _reflection.GeneratedProtocolMessageType('RemoveInboundResponse', (_message.Message,), {
  'DESCRIPTOR' : _REMOVEINBOUNDRESPONSE,
  '__module__' : 'app.proxyman.command.command_pb2'
  # @@protoc_insertion_point(class_scope:xray.app.proxyman.command.RemoveInboundResponse)
  })
_sym_db.RegisterMessage(RemoveInboundResponse)

AlterInboundRequest = _reflection.GeneratedProtocolMessageType('AlterInboundRequest', (_message.Message,), {
  'DESCRIPTOR' : _ALTERINBOUNDREQUEST,
  '__module__' : 'app.proxyman.command.command_pb2'
  # @@protoc_insertion_point(class_scope:xray.app.proxyman.command.AlterInboundRequest)
  })
_sym_db.RegisterMessage(AlterInboundRequest)

AlterInboundResponse = _reflection.GeneratedProtocolMessageType('AlterInboundResponse', (_message.Message,), {
  'DESCRIPTOR' : _ALTERINBOUNDRESPONSE,
  '__module__' : 'app.proxyman.command.command_pb2'
  # @@protoc_insertion_point(class_scope:xray.app.proxyman.command.AlterInboundResponse)
  })
_sym_db.RegisterMessage(AlterInboundResponse)

AddOutboundRequest = _reflection.GeneratedProtocolMessageType('AddOutboundRequest', (_message.Message,), {
  'DESCRIPTOR' : _ADDOUTBOUNDREQUEST,
  '__module__' : 'app.proxyman.command.command_pb2'
  # @@protoc_insertion_point(class_scope:xray.app.proxyman.command.AddOutboundRequest)
  })
_sym_db.RegisterMessage(AddOutboundRequest)

AddOutboundResponse = _reflection.GeneratedProtocolMessageType('AddOutboundResponse', (_message.Message,), {
  'DESCRIPTOR' : _ADDOUTBOUNDRESPONSE,
  '__module__' : 'app.proxyman.command.command_pb2'
  # @@protoc_insertion_point(class_scope:xray.app.proxyman.command.AddOutboundResponse)
  })
_sym_db.RegisterMessage(AddOutboundResponse)

RemoveOutboundRequest = _reflection.GeneratedProtocolMessageType('RemoveOutboundRequest', (_message.Message,), {
  'DESCRIPTOR' : _REMOVEOUTBOUNDREQUEST,
  '__module__' : 'app.proxyman.command.command_pb2'
  # @@protoc_insertion_point(class_scope:xray.app.proxyman.command.RemoveOutboundRequest)
  })
_sym_db.RegisterMessage(RemoveOutboundRequest)

RemoveOutboundResponse = _reflection.GeneratedProtocolMessageType('RemoveOutboundResponse', (_message.Message,), {
  'DESCRIPTOR' : _REMOVEOUTBOUNDRESPONSE,
  '__module__' : 'app.proxyman.command.command_pb2'
  # @@protoc_insertion_point(class_scope:xray.app.proxyman.command.RemoveOutboundResponse)
  })
_sym_db.RegisterMessage(RemoveOutboundResponse)

AlterOutboundRequest = _reflection.GeneratedProtocolMessageType('AlterOutboundRequest', (_message.Message,), {
  'DESCRIPTOR' : _ALTEROUTBOUNDREQUEST,
  '__module__' : 'app.proxyman.command.command_pb2'
  # @@protoc_insertion_point(class_scope:xray.app.proxyman.command.AlterOutboundRequest)
  })
_sym_db.RegisterMessage(AlterOutboundRequest)

AlterOutboundResponse = _reflection.GeneratedProtocolMessageType('AlterOutboundResponse', (_message.Message,), {
  'DESCRIPTOR' : _ALTEROUTBOUNDRESPONSE,
  '__module__' : 'app.proxyman.command.command_pb2'
  # @@protoc_insertion_point(class_scope:xray.app.proxyman.command.AlterOutboundResponse)
  })
_sym_db.RegisterMessage(AlterOutboundResponse)

Config = _reflection.GeneratedProtocolMessageType('Config', (_message.Message,), {
  'DESCRIPTOR' : _CONFIG,
  '__module__' : 'app.proxyman.command.command_pb2'
  # @@protoc_insertion_point(class_scope:xray.app.proxyman.command.Config)
  })
_sym_db.RegisterMessage(Config)

_HANDLERSERVICE = DESCRIPTOR.services_by_name['HandlerService']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\035com.xray.app.proxyman.commandP\001Z.github.com/xtls/xray-core/app/proxyman/command\252\002\031Xray.App.Proxyman.Command'
  _ADDUSEROPERATION._serialized_start=147
  _ADDUSEROPERATION._serialized_end=207
  _REMOVEUSEROPERATION._serialized_start=209
  _REMOVEUSEROPERATION._serialized_end=245
  _ADDINBOUNDREQUEST._serialized_start=247
  _ADDINBOUNDREQUEST._serialized_end=316
  _ADDINBOUNDRESPONSE._serialized_start=318
  _ADDINBOUNDRESPONSE._serialized_end=338
  _REMOVEINBOUNDREQUEST._serialized_start=340
  _REMOVEINBOUNDREQUEST._serialized_end=375
  _REMOVEINBOUNDRESPONSE._serialized_start=377
  _REMOVEINBOUNDRESPONSE._serialized_end=400
  _ALTERINBOUNDREQUEST._serialized_start=402
  _ALTERINBOUNDREQUEST._serialized_end=489
  _ALTERINBOUNDRESPONSE._serialized_start=491
  _ALTERINBOUNDRESPONSE._serialized_end=513
  _ADDOUTBOUNDREQUEST._serialized_start=515
  _ADDOUTBOUNDREQUEST._serialized_end=587
  _ADDOUTBOUNDRESPONSE._serialized_start=589
  _ADDOUTBOUNDRESPONSE._serialized_end=610
  _REMOVEOUTBOUNDREQUEST._serialized_start=612
  _REMOVEOUTBOUNDREQUEST._serialized_end=648
  _REMOVEOUTBOUNDRESPONSE._serialized_start=650
  _REMOVEOUTBOUNDRESPONSE._serialized_end=674
  _ALTEROUTBOUNDREQUEST._serialized_start=676
  _ALTEROUTBOUNDREQUEST._serialized_end=764
  _ALTEROUTBOUNDRESPONSE._serialized_start=766
  _ALTEROUTBOUNDRESPONSE._serialized_end=789
  _CONFIG._serialized_start=791
  _CONFIG._serialized_end=799
  _HANDLERSERVICE._serialized_start=802
  _HANDLERSERVICE._serialized_end=1511
# @@protoc_insertion_point(module_scope)
