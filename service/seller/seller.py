from flask_restful import Resource


class SellerTest(Resource):

    def get(self):
        return "<h1>Hello to world from seller side</h1>"
