from flask import Blueprint
from service.buyer import *

buyer_routes = Blueprint('buyer', __name__, url_prefix="/api/buyer")
buyer_routes.add_url_rule('/', view_func=BuyerTest.as_view('buyer_test'))
