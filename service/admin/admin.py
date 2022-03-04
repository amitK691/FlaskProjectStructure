from flask import Flask
from flask_restful import Resource


class AdminTest(Resource):

    def get(self):
        return "<h1> Hello to world from admin</h1>"
