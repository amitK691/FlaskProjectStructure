from flask import Blueprint
from service.accounts import *

accounts_routes = Blueprint('accounts', __name__, url_prefix='/api/account')

accounts_routes.add_url_rule('/', view_func=Test.as_view('Test'))
accounts_routes.add_url_rule('register/', view_func=SingUp.as_view('register'))
accounts_routes.add_url_rule('login/', view_func=LogIn.as_view('login'))    
accounts_routes.add_url_rule('get-users/', view_func=GetUsers.as_view('get_users'))
accounts_routes.add_url_rule('get-user/<int:id>/', view_func=GetUser.as_view('get_user'))
accounts_routes.add_url_rule('user-update/<int:id>/', view_func=UpdateUser.as_view('user_update'))
