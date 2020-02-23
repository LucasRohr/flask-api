# Importamos as classes API e Resource
from flask_restful import Api, Resource
from datetime import date

from apps.controller.users.list_users_resource import AdminListUsers
from apps.controller.users.search_user_by_id_resource import AdminSearchUser
from apps.controller.users.edit_user_resource import AdminEditUser
from apps.controller.users.delete_user_resource import AdminDeleteUser
from apps.controller.users.register_resource import SignUp


# Criamos uma classe que extende de Resource
class Index(Resource):

    # Definimos a operação get do protocolo http
    def get(self):
        # retornamos um simples dicionário que será automáticamente
        # retornado em json pelo flask
        return {
            'ehUsGuri': True,
            'date': str(date.today())
        }


# Instânciamos a API do FlaskRestful
api = Api()


def configure_api(app):

    # adicionamos na rota '/' a sua classe correspondente Index
    api.add_resource(Index, '/')

    #Register user
    api.add_resource(SignUp, '/register')

    #List Users
    api.add_resource(AdminListUsers, '/admin/users/<int:page_id>')

    #Get user by ID
    api.add_resource(AdminSearchUser, '/admin/users/<string:user_id>')

    #Edit user
    api.add_resource(AdminEditUser, '/admin/users/edit/<string:user_id>')

    #Delete user
    api.add_resource(AdminDeleteUser, '/admin/users/delete/<string:user_id>')

    # inicializamos a api com as configurações do flask vinda por parâmetro
    api.init_app(app)
