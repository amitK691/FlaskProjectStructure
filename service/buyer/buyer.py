from flask_restful import Resource


class BuyerTest(Resource):

    def get(self):
        return "<h1>Hello To world from Buyer side</h1>"
