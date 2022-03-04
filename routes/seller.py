from flask import Blueprint
from service.seller import *

seller_routes = Blueprint('seller', __name__, url_prefix='/api/seller')
seller_routes.add_url_rule('/', view_func=SellerTest.as_view('seller_test'))
