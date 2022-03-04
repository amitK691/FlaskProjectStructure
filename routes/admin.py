from flask import Blueprint
from flask_restful import Api
from service.admin import *

admin_routes = Blueprint('executive', __name__, url_prefix="/api/admin")
admin_routes.add_url_rule('/', view_func=AdminTest.as_view('test_view'))
