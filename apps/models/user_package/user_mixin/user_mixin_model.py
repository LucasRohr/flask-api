from datetime import datetime

from mongoengine import (
    BooleanField,
    DateTimeField,
    EmailField,
    EmbeddedDocumentField,
    StringField,
    IntField
)

from apps.db import db
from apps.models.user_package.role.roles import Roles


class UserMixin(db.Document):
    meta = {
        'abstract': True,
        'ordering': ['email']
    }

    email = EmailField(required=True, unique=True)
    password = StringField(required=True)
    roles = EmbeddedDocumentField(Roles, default=Roles)
    created = DateTimeField(default=datetime.now)
    active = BooleanField(default=False)

    def is_active(self):
        return self.active

    def is_admin(self):
        return self.roles.admin
