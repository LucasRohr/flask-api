from flask import request
from flask_restful import Resource

from apps.responses.responses import resp_exception, resp_ok

from apps.validators.page_size_validator import validate_page_size

from apps.constants.messages import MSG_RESOURCE_FETCHED_PAGINATED

from apps.models.user_package.user.user_model import User
from apps.models.user_package.schema.user_schema import UserSchema


class AdminListUsers(Resource):

    def get(self, page_id=1):
        schema = UserSchema(many=True)
        page_size = 10

        page_size = validate_page_size(request, page_size)

        try:
            users_list = User.objects().paginate(page_id, page_size)
        except Exception as e:
            return resp_exception('Users', description=e.__str__())

        extra = {
            'page': users_list.page,
            'pages': users_list.pages,
            'total': users_list.total,
            'params': {
                'page_size': page_size
            }
        }

        result = schema.dump(users_list.items)

        return resp_ok(
            'Users',
            MSG_RESOURCE_FETCHED_PAGINATED.format('Usuários'),
            data=result.data,
            **extra
        )
