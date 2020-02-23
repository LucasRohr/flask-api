from flask import request
from flask_restful import Resource
from mongoengine import NotUniqueError, ValidationError

from ..utils.user_utils import get_user_by_id
from apps.models.user_package.user.user_model import User

from apps.responses.responses import resp_exception, resp_already_exists, resp_ok
from apps.constants.messages import MSG_INVALID_DATA, MSG_RESOURCE_DELETED


class AdminDeleteUser(Resource):

    def delete(self, user_id):
        result = None
        user = get_user_by_id(user_id)

        if not isinstance(user, User):
            return user

        try:
            user.active = False
            user.save()

        except NotUniqueError:
            return resp_already_exists('Users', 'usuário')

        except ValidationError as e:
            return resp_exception('Users', msg=MSG_INVALID_DATA, description=e.__str__())

        except Exception as e:
            return resp_exception('Users', description=e.__str__())

        return resp_ok(
            'Users',
            MSG_RESOURCE_DELETED.format('Usuário'),
            {
                'user_id': user_id
            }
        )
