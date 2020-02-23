from flask import request
from flask_restful import Resource

from apps.models.user_package.schema.user_schema import UserSchema
from apps.models.user_package.user.user_model import User

from mongoengine.errors import FieldDoesNotExist

from apps.responses.responses import resp_exception, resp_ok

from ..utils.user_utils import get_user_by_id


class AdminSearchUser(Resource):

    def get(self, user_id):
        result = None
        user = None
        schema = UserSchema(many=False)

        user = get_user_by_id(user_id)

        result = schema.dump(user)

        return resp_ok(
            'Users',
            'Usuário encontrado',
            date=result.data
        )
