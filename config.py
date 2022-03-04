import os
from dotenv import load_dotenv
load_dotenv()
# class BaseConfig:
#     SECRET_KEY = os.environ.get('SECRET_KEY')
#     SQLALCHEMY_TRACK_MODIFICATIONS = False
#
#     # MAIL_SERVER = 'smtp.googlemail.com'
#     # MAIL_PORT = 587
#     # MAIL_USE_TLS = True
#     # MAIL_USERNAME = os.environ.get('MAIL_USERNAME') or 'infooveriq@gmail.com'
#     # MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD') or 'password'
#     # MAIL_DEFAULT_SENDER = MAIL_USERNAME
#
#
# class DevelopementConfig(BaseConfig):
#     DEBUG = True
#     SQLALCHEMY_DATABASE_URI = os.environ["SQLALCHEMY_DATABASE_URI"]
#     SECRET_KEY = BaseConfig.SECRET_KEY
#     SQLALCHEMY_TRACK_MODIFICATIONS = BaseConfig.SQLALCHEMY_TRACK_MODIFICATIONS


class Config(object):
    SQLALCHEMY_DATABASE_URI = os.environ["SQLALCHEMY_DATABASE_URI"]
    SECRET_KEY = os.environ["SECRET_KEY"]
    SQLALCHEMY_TRACK_MODIFICATIONS = os.environ["SQLALCHEMY_TRACK_MODIFICATIONS"]
