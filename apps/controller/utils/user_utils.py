from mongoengine import FieldDoesNotExist, DoesNotExist, MultipleObjectsReturned

from apps.models.user_package.user.user_model import User
from apps.responses.responses import resp_does_not_exist, resp_exception


def get_user_by_id(user_id: str):
    try:
        # buscamos todos os usuários da base utilizando o paginate
        return User.objects.get(id=user_id)

    except DoesNotExist as e:
        return resp_does_not_exist('Users', 'Usuário')

    except FieldDoesNotExist as e:
        return resp_exception('Users', description=e.__str__())

    except Exception as e:
        return resp_exception('Users', description=e.__str__())


def check_user_email_exists(email: str, instance=None):
    user = None

    try:
        user = User.objects().get(email=email)
    except DoesNotExist:
        return False
    except MultipleObjectsReturned:
        return True

    if instance and instance.id == user.id:
        return False

    return True
