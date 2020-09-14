# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads_v4/proto/resources/language_constant.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/ads/googleads_v4/proto/resources/language_constant.proto',
  package='google.ads.googleads.v4.resources',
  syntax='proto3',
  serialized_options=_b('\n%com.google.ads.googleads.v4.resourcesB\025LanguageConstantProtoP\001ZJgoogle.golang.org/genproto/googleapis/ads/googleads/v4/resources;resources\242\002\003GAA\252\002!Google.Ads.GoogleAds.V4.Resources\312\002!Google\\Ads\\GoogleAds\\V4\\Resources\352\002%Google::Ads::GoogleAds::V4::Resources'),
  serialized_pb=_b('\n?google/ads/googleads_v4/proto/resources/language_constant.proto\x12!google.ads.googleads.v4.resources\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1egoogle/protobuf/wrappers.proto\x1a\x1cgoogle/api/annotations.proto\"\xf8\x02\n\x10LanguageConstant\x12H\n\rresource_name\x18\x01 \x01(\tB1\xe0\x41\x03\xfa\x41+\n)googleads.googleapis.com/LanguageConstant\x12,\n\x02id\x18\x02 \x01(\x0b\x32\x1b.google.protobuf.Int64ValueB\x03\xe0\x41\x03\x12/\n\x04\x63ode\x18\x03 \x01(\x0b\x32\x1c.google.protobuf.StringValueB\x03\xe0\x41\x03\x12/\n\x04name\x18\x04 \x01(\x0b\x32\x1c.google.protobuf.StringValueB\x03\xe0\x41\x03\x12\x33\n\ntargetable\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.BoolValueB\x03\xe0\x41\x03:U\xea\x41R\n)googleads.googleapis.com/LanguageConstant\x12%languageConstants/{language_constant}B\x82\x02\n%com.google.ads.googleads.v4.resourcesB\x15LanguageConstantProtoP\x01ZJgoogle.golang.org/genproto/googleapis/ads/googleads/v4/resources;resources\xa2\x02\x03GAA\xaa\x02!Google.Ads.GoogleAds.V4.Resources\xca\x02!Google\\Ads\\GoogleAds\\V4\\Resources\xea\x02%Google::Ads::GoogleAds::V4::Resourcesb\x06proto3')
  ,
  dependencies=[google_dot_api_dot_field__behavior__pb2.DESCRIPTOR,google_dot_api_dot_resource__pb2.DESCRIPTOR,google_dot_protobuf_dot_wrappers__pb2.DESCRIPTOR,google_dot_api_dot_annotations__pb2.DESCRIPTOR,])




_LANGUAGECONSTANT = _descriptor.Descriptor(
  name='LanguageConstant',
  full_name='google.ads.googleads.v4.resources.LanguageConstant',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='resource_name', full_name='google.ads.googleads.v4.resources.LanguageConstant.resource_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\340A\003\372A+\n)googleads.googleapis.com/LanguageConstant'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='id', full_name='google.ads.googleads.v4.resources.LanguageConstant.id', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\340A\003'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='code', full_name='google.ads.googleads.v4.resources.LanguageConstant.code', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\340A\003'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='google.ads.googleads.v4.resources.LanguageConstant.name', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\340A\003'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='targetable', full_name='google.ads.googleads.v4.resources.LanguageConstant.targetable', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\340A\003'), file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=_b('\352AR\n)googleads.googleapis.com/LanguageConstant\022%languageConstants/{language_constant}'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=225,
  serialized_end=601,
)

_LANGUAGECONSTANT.fields_by_name['id'].message_type = google_dot_protobuf_dot_wrappers__pb2._INT64VALUE
_LANGUAGECONSTANT.fields_by_name['code'].message_type = google_dot_protobuf_dot_wrappers__pb2._STRINGVALUE
_LANGUAGECONSTANT.fields_by_name['name'].message_type = google_dot_protobuf_dot_wrappers__pb2._STRINGVALUE
_LANGUAGECONSTANT.fields_by_name['targetable'].message_type = google_dot_protobuf_dot_wrappers__pb2._BOOLVALUE
DESCRIPTOR.message_types_by_name['LanguageConstant'] = _LANGUAGECONSTANT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

LanguageConstant = _reflection.GeneratedProtocolMessageType('LanguageConstant', (_message.Message,), dict(
  DESCRIPTOR = _LANGUAGECONSTANT,
  __module__ = 'google.ads.googleads_v4.proto.resources.language_constant_pb2'
  ,
  __doc__ = """A language.
  
  
  Attributes:
      resource_name:
          Output only. The resource name of the language constant.
          Language constant resource names have the form:
          ``languageConstants/{criterion_id}``
      id:
          Output only. The ID of the language constant.
      code:
          Output only. The language code, e.g. "en\_US", "en\_AU", "es",
          "fr", etc.
      name:
          Output only. The full name of the language in English, e.g.,
          "English (US)", "Spanish", etc.
      targetable:
          Output only. Whether the language is targetable.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v4.resources.LanguageConstant)
  ))
_sym_db.RegisterMessage(LanguageConstant)


DESCRIPTOR._options = None
_LANGUAGECONSTANT.fields_by_name['resource_name']._options = None
_LANGUAGECONSTANT.fields_by_name['id']._options = None
_LANGUAGECONSTANT.fields_by_name['code']._options = None
_LANGUAGECONSTANT.fields_by_name['name']._options = None
_LANGUAGECONSTANT.fields_by_name['targetable']._options = None
_LANGUAGECONSTANT._options = None
# @@protoc_insertion_point(module_scope)