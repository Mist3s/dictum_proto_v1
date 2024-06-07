# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proto/accrual.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from dictum_proto.proto import account_pb2 as proto_dot_account__pb2
from dictum_proto.proto import attachment_pb2 as proto_dot_attachment__pb2
from dictum_proto.proto import accrual_type_pb2 as proto_dot_accrual__type__pb2
from dictum_proto.proto import article_pb2 as proto_dot_article__pb2
from dictum_proto.proto import color_pb2 as proto_dot_color__pb2
from dictum_proto.proto import comment_pb2 as proto_dot_comment__pb2
from dictum_proto.proto import currency_pb2 as proto_dot_currency__pb2
from dictum_proto.proto import entity_pb2 as proto_dot_entity__pb2
from dictum_proto.proto import operation_pb2 as proto_dot_operation__pb2
from dictum_proto.proto import payment_type_pb2 as proto_dot_payment__type__pb2
from dictum_proto.proto import signature_pb2 as proto_dot_signature__pb2
from dictum_proto.proto import source_pb2 as proto_dot_source__pb2
from dictum_proto.proto import status_pb2 as proto_dot_status__pb2
from dictum_proto.proto import user_pb2 as proto_dot_user__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x13proto/accrual.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x13proto/account.proto\x1a\x16proto/attachment.proto\x1a\x18proto/accrual_type.proto\x1a\x13proto/article.proto\x1a\x11proto/color.proto\x1a\x13proto/comment.proto\x1a\x14proto/currency.proto\x1a\x12proto/entity.proto\x1a\x15proto/operation.proto\x1a\x18proto/payment_type.proto\x1a\x15proto/signature.proto\x1a\x12proto/source.proto\x1a\x12proto/status.proto\x1a\x10proto/user.proto\"\xe2\x0e\n\x07\x41\x63\x63rual\x12\x10\n\x08\x65vent_id\x18\x01 \x01(\x05\x12\x17\n\x0f\x63onglomerate_id\x18\x02 \x01(\x05\x12\x18\n\x10one_transfer_pay\x18\x03 \x01(\x08\x12\x14\n\x0coperation_id\x18\x04 \x01(\x05\x12\x15\n\rcurrency_code\x18\x05 \x01(\t\x12\x1a\n\x04type\x18\x06 \x01(\x0e\x32\x0c.AccrualType\x12\x12\n\narticle_id\x18\x07 \x01(\x05\x12\x12\n\nsys_period\x18\x08 \x01(\t\x12\x16\n\x0einvoice_number\x18\t \x01(\t\x12\x12\n\nproject_id\x18\n \x01(\x05\x12\x1c\n\x14recipient_account_id\x18\x0b \x01(\x05\x12\x18\n\x10payer_account_id\x18\x0c \x01(\x05\x12\x12\n\nis_initial\x18\r \x01(\x08\x12\"\n\x0cpayment_type\x18\x0e \x01(\x0e\x32\x0c.PaymentType\x12!\n\x19has_other_money_recipient\x18\x0f \x01(\x08\x12\x13\n\x0b\x61pprover_id\x18\x10 \x01(\x05\x12\x15\n\rpayer_user_id\x18\x11 \x01(\x05\x12\x14\n\x0c\x61llow_payout\x18\x12 \x01(\x08\x12\x15\n\rresource_name\x18\x13 \x01(\t\x12\x12\n\nsource_key\x18\x14 \x01(\t\x12\x19\n\npayer_user\x18\x15 \x01(\x0b\x32\x05.User\x12\x17\n\x08\x61pprover\x18\x16 \x01(\x0b\x32\x05.User\x12\x1d\n\toperation\x18\x17 \x01(\x0b\x32\n.Operation\x12\x1b\n\x08\x63urrency\x18\x18 \x01(\x0b\x32\t.Currency\x12#\n\x11recipient_account\x18\x19 \x01(\x0b\x32\x08.Account\x12\x1f\n\rpayer_account\x18\x1a \x01(\x0b\x32\x08.Account\x12\x19\n\x07\x61rticle\x18\x1b \x01(\x0b\x32\x08.Article\x12\x10\n\x08payer_id\x18\x1c \x01(\x05\x12\x14\n\x0crecipient_id\x18\x1d \x01(\x05\x12\x0e\n\x06\x61mount\x18\x1e \x01(\x01\x12\x18\n\x10\x61llocated_amount\x18\x1f \x01(\x01\x12\x14\n\x0cpayout_proof\x18  \x01(\t\x12\x0c\n\x04note\x18! \x01(\t\x12\x11\n\ttaxAmount\x18\" \x01(\x01\x12\x12\n\ntaxPercent\x18# \x01(\x01\x12\x14\n\x0ctaxInclusive\x18$ \x01(\x08\x12\x1b\n\ndatasource\x18% \x01(\x0e\x32\x07.Source\x12\x15\n\x05\x63olor\x18& \x01(\x0e\x32\x06.Color\x12\x38\n\x14\x66ull_allocation_time\x18\' \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x16\n\x05payer\x18( \x01(\x0b\x32\x07.Entity\x12\x1a\n\trecipient\x18) \x01(\x0b\x32\x07.Entity\x12\x30\n\x0cperform_time\x18* \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x34\n\x10payment_due_time\x18+ \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12/\n\x0bpayout_date\x18, \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12,\n\x08pay_time\x18- \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12/\n\x0b\x63reate_time\x18. \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x17\n\x06status\x18/ \x01(\x0e\x32\x07.Status\x12 \n\x0b\x61ttachments\x18\x30 \x03(\x0b\x32\x0b.Attachment\x12\x14\n\x0cinitiator_id\x18\x31 \x01(\x05\x12\x11\n\tauthor_id\x18\x32 \x01(\x05\x12\x14\n\x0c\x63onsignee_id\x18\x33 \x01(\x05\x12\x11\n\tpublished\x18\x34 \x01(\x08\x12\x0f\n\x07\x61udited\x18\x35 \x01(\x08\x12 \n\x18require_primary_document\x18\x36 \x01(\x08\x12\x18\n\x10payer_article_id\x18\x37 \x01(\x05\x12\x1c\n\x14\x63onsignee_article_id\x18\x38 \x01(\x05\x12\x1c\n\x14recipient_article_id\x18\x39 \x01(\x05\x12\x12\n\nprimary_id\x18: \x01(\x05\x12\x11\n\tconfirmed\x18\x43 \x01(\x08\x12\x1e\n\x0cpayerArticle\x18; \x01(\x0b\x32\x08.Article\x12\"\n\x10\x63onsigneeArticle\x18< \x01(\x0b\x32\x08.Article\x12\"\n\x10recipientArticle\x18= \x01(\x0b\x32\x08.Article\x12\x1a\n\x08\x63omments\x18> \x03(\x0b\x32\x08.Comment\x12\x15\n\x06\x61uthor\x18? \x01(\x0b\x32\x05.User\x12\x1a\n\tinitiator\x18@ \x01(\x0b\x32\x07.Entity\x12\x1a\n\tconsignee\x18\x41 \x01(\x0b\x32\x07.Entity\x12\x1e\n\nsignatures\x18\x42 \x03(\x0b\x32\n.Signature\x12\r\n\x05total\x18\x44 \x01(\x01\x12\x18\n\x10\x63\x61ncel_mark_paid\x18\x45 \x01(\x08\x42&Z$github.com/AlexKenbo/dictum_proto/gob\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'proto.accrual_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z$github.com/AlexKenbo/dictum_proto/go'
  _globals['_ACCRUAL']._serialized_start=361
  _globals['_ACCRUAL']._serialized_end=2251
# @@protoc_insertion_point(module_scope)
