from flask import Flask
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_migrate import Migrate
from routes.accounts import accounts_routes
from routes.admin import admin_routes
from routes.buyer import buyer_routes
from routes.seller import seller_routes

# from models.accounts import
from models.accounts import *

migrate = Migrate()


def create_app(Config):
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    migrate.init_app(app, db)
    superuser = Admin(app)
    with app.app_context():
        db.create_all()

    superuser.add_view(ModelView(User, db.session, endpoint='user'))
    superuser.add_view(ModelView(Role, db.session, endpoint='role'))
    app.register_blueprint(accounts_routes)
    app.register_blueprint(admin_routes)
    app.register_blueprint(buyer_routes)
    app.register_blueprint(seller_routes)

    return app
