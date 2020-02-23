from mongoengine import (
    BooleanField,
    EmbeddedDocument,
)


class Roles(EmbeddedDocument):
    admin = BooleanField(default=False)
