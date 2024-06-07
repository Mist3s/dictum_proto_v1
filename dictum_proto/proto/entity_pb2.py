# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proto/entity.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from dictum_proto.proto import entity_type_pb2 as proto_dot_entity__type__pb2
from dictum_proto.proto import telegram_user_pb2 as proto_dot_telegram__user__pb2
from dictum_proto.proto import country_pb2 as proto_dot_country__pb2
from dictum_proto.proto import agent_pb2 as proto_dot_agent__pb2
from dictum_proto.proto import entity_source_pb2 as proto_dot_entity__source__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x12proto/entity.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x17proto/entity_type.proto\x1a\x19proto/telegram_user.proto\x1a\x13proto/country.proto\x1a\x11proto/agent.proto\x1a\x19proto/entity_source.proto\"\xd4\x03\n\x06\x45ntity\x12\x11\n\tentity_id\x18\x01 \x01(\x05\x12\x17\n\x0f\x63onglomerate_id\x18\x02 \x01(\x05\x12\r\n\x05title\x18\x03 \x01(\t\x12\x19\n\x04type\x18\x04 \x01(\x0e\x32\x0b.EntityType\x12\x10\n\x08is_agent\x18\x05 \x01(\x08\x12\x16\n\x0eis_employee_of\x18\x06 \x01(\x08\x12\r\n\x05\x65mail\x18\t \x01(\t\x12\r\n\x05phone\x18\x0b \x01(\t\x12\x0f\n\x07\x61\x64\x64ress\x18\r \x01(\t\x12\x18\n\x10telegram_user_id\x18\x0f \x01(\x05\x12\x14\n\x0c\x63ountry_code\x18\x11 \x01(\t\x12\x12\n\nsource_key\x18\x13 \x01(\t\x12$\n\rtelegram_user\x18\x15 \x01(\x0b\x32\r.TelegramUser\x12\x19\n\x07\x63ountry\x18\x17 \x01(\x0b\x32\x08.Country\x12\x15\n\x05\x61gent\x18\x19 \x01(\x0b\x32\x06.Agent\x12\x1e\n\x07sources\x18\x1b \x03(\x0b\x32\r.EntitySource\x12\x1a\n\x12\x63ontact_creator_id\x18\x1c \x01(\x05\x12\x12\n\nalias_code\x18\x1d \x01(\t\x12/\n\x0b\x63reate_time\x18\x1e \x01(\x0b\x32\x1a.google.protobuf.TimestampB&Z$github.com/AlexKenbo/dictum_proto/gob\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'proto.entity_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z$github.com/AlexKenbo/dictum_proto/go'
  _globals['_ENTITY']._serialized_start=175
  _globals['_ENTITY']._serialized_end=643
# @@protoc_insertion_point(module_scope)
