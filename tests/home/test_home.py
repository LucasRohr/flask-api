from unittest import TestCase
import sys

sys.path.insert(1, '../../apps/models/user_package/user')
sys.path.insert(2, '../../apps/models/user_package/schema')

from user_model import User


class HomeTests(TestCase):

    def test_user(self):
        user = User(email='teste@teste.com', password='123456', full_name='Teste OSchema', cpf_cnpj="00609568019")
        # schema = user_schema.UserSchema()
        # result = schema.dump(user)
        print(user)
