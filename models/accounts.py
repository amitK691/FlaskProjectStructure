import uuid

from flask import make_response, jsonify
from flask_sqlalchemy import SQLAlchemy
from typing import Callable
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from sqlalchemy.orm import backref
from models.base import BaseModel, db
# from sqlalchemy.orm import declarative_base
from werkzeug.security import check_password_hash, generate_password_hash


# Base = declarative_base()


# class MySQLAlchemy(SQLAlchemy):
#     Column: Callable
#     String: Callable
#     Integer: Callable
#
#
# db = MySQLAlchemy()


class Role(BaseModel):
    
    __tablename__ = 'roles'

    role_name = db.Column(db.String(50), unique=True, nullable=False)


def generate_uuid():
    return str(uuid.uuid4())


class User(BaseModel):
    uuid = db.Column(db.String(255), unique=True, default=generate_uuid())
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
    role = db.relationship('Role', backref=backref('role', uselist=False))

    def json(self):
        return {'username': self.username,
                'email': self.email,
                'uuid': self.uuid,
                }

    @staticmethod
    def get_all_user():
        return [User.json(user) for user in User.query.all()]

    @staticmethod
    def get_user(id):
        query = User.query.filter_by(id=id).first()
        js = {
            'username': query.username,
            'email': query.email
        }
        return js

    @staticmethod
    def update_user(id, _username):
        user_to_update = User.query.filter_by(id=id).first()
        if user_to_update:
            user_to_update.username = _username
            db.session.commit()
            data = {
                'message': 'User updated successfully',
                'status': '200'
            }
            return make_response(jsonify({'data': data}))
        else:
            response = {
                'message': 'user not exists',
                'status': '401'
            }
            return make_response(jsonify({'error': response}))


