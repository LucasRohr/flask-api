from apps.models.adress.adress import Address
from apps.models.user_package.user_mixin.user_mixin_model import UserMixin


from mongoengine import (
    EmbeddedDocumentField,
    StringField,
    ListField
)


class User(UserMixin):
    meta = {'collection': 'users'}

    full_name = StringField(required=True)
    cpf_cnpj = StringField(default='')
    addresses = ListField(EmbeddedDocumentField(Address, default=Address))
