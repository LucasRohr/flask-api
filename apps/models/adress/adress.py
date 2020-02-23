from mongoengine import (
    EmbeddedDocument,
    StringField
)


class Address(EmbeddedDocument):
    """
    Default implementation for address fields
    """
    meta = {
        'ordering': ['zip_code']
    }
    zip_code = StringField(default='')
    address = StringField(default='')
    number = StringField(default='')
    complement = StringField(default='')
    neighborhood = StringField(default='')
    city = StringField(default='')
    city_id = StringField(default='')
    state = StringField(default='')
    country = StringField(default='BRA')
