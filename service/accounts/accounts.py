import datetime
import json
import uuid
from config import Config
import jwt
from flask_restful import Resource
from flask import jsonify, request, make_response, Response
from models.accounts import *
from werkzeug.security import generate_password_hash
from functools import wraps
from Tools.scripts.parse_html5_entities import get_json


def token_required(f):
    wraps(f)

    def decorated(*args, **kwargs):
        token = None

        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']

        if not token:
            return jsonify({'message': 'token is missing'})

        try:
            print(Config.SECRET_KEY)
            data = jwt.decode(token, Config.SECRET_KEY)
            current_user = User.query.filter_by(uuid=data['uuid']).first()

        except Exception as e:

            return jsonify({'message': 'token is invalid'}), 401

        return f(current_user, *args, **kwargs)

    return decorated()


class Test(Resource):
    def get(self):
        # return "<h1>Hello world This is account section</h1>"
        data = {
            'user': 'amit',
            'id': '4'
        }

        return jsonify({'data': data})


class SingUp(Resource):

    def post(self):
        data = json.loads(request.data)

        print(data.get('username'))
        user = User.query.filter_by(email=data.get('email')).first()
        if not user:
            user = User(email=data.get('email'),
                        password=generate_password_hash(data.get('password')),
                        username=data.get('username'))
            db.session.add(user)
            db.session.commit()
            return make_response('Successfully registered.', 201)
        else:
            return make_response('User already exists. Please Log in', 202)


class LogIn(Resource):

    def get(self):
        auth = request.authorization

        if not auth or not auth.username or not auth.password:
            return make_response('Could not verify', 401, {
                'WWW-Authenticate': 'Basic realm="Login required!"'})

        user = User.query.filter_by(name=auth.username).first()

        if not user:
            return make_response('Could not verify', 401, {
                'WWW-Authenticate': 'Basic realm="Login required!"'})

        if check_password_hash(user.password, auth.password):
            token = jwt.encode({'public_id': user.public_id,
                                'exp': datetime.datetime.utcnow() + datetime.timedelta(
                                    minutes=30)}, app.config['SECRET_KEY'])

            return jsonify({'token': token.decode('UTF-8')})

        return make_response('Could not verify', 401, {
            'WWW-Authenticate': 'Basic realm="Login required!"'})


class GetUsers(Resource):

    def get(self):
        return jsonify({'users_data': User.get_all_user()})


class GetUser(Resource):

    def get(self, id):
        return jsonify({'user': User.get_user(id)})


class UpdateUser(Resource):

    def get(self, id):
        data = request.args.get('username')
        # data = json.loads(request.data)
        # print(data.get('username'))
        # User.update_user(id, data)
        # data = {
        #         'message': 'User updated successfully',
        #         'status': '200'
        # }
        return User.update_user(id, data)

