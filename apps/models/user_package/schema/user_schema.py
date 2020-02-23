from marshmallow import Schema
from marshmallow.fields import Email, Str, Boolean, Nested
from apps.constants.messages import MSG_FIELD_REQUIRED


class UserRegistrationSchema(Schema):
    full_name = Str(required=True, error_messages={'required': MSG_FIELD_REQUIRED})
    email = Email(required=True, error_messages={'required': MSG_FIELD_REQUIRED})
    password = Str(required=True, error_messages={'required': MSG_FIELD_REQUIRED})


class UserSchema(Schema):
    full_name = Str(required=True, error_messages={'required': MSG_FIELD_REQUIRED})
    email = Email(required=True, error_messages={'required': MSG_FIELD_REQUIRED})
    cpf_cnpj = Str(required=True)
    active = Boolean()

class EditUserSchema(Schema):
    full_name = Str()
    email = Email()
    cpf_cnpj = Str()
