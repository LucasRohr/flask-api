from flask import request
from flask_restful import Resource
from mongoengine import NotUniqueError

from apps.responses.responses import resp_ok, resp_data_invalid, resp_already_exists

from apps.constants.messages import MSG_RESOURCE_UPDATED, MSG_INVALID_DATA, MSG_ALREADY_EXISTS

from apps.models.user_package.user.user_model import User
from apps.models.user_package.schema.user_schema import UserSchema, EditUserSchema

from ..utils.user_utils import get_user_by_id, check_user_email_exists


class AdminEditUser(Resource):

    def put(self, user_id):
        result = None
        user = None

        req_data = request.get_json() or None

        user_schema = UserSchema()
        edi_user_schema = EditUserSchema()

        if req_data is None:
            return resp_data_invalid('Users', [], msg=MSG_INVALID_DATA)

        user = get_user_by_id(user_id)

        if not isinstance(user, User):
            return user

        data, errors = edi_user_schema.load(req_data)

        if errors:
            return resp_data_invalid('Users', errors)

        email = data.get('Email', None)

        if email and check_user_email_exists(email):
            return resp_data_invalid(
                'Users',
                [{ 'email', [MSG_ALREADY_EXISTS.format('usuário')] }]
            )

        try:
            for key in data.keys():
                user[key] = data[key]

            user.save()
        except NotUniqueError:
            return resp_already_exists('Users', 'usuário')

        result = user_schema.dump(user)

        return resp_ok(
            'Users',
            MSG_RESOURCE_UPDATED,
            data=result.data
        )
