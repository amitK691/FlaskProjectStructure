from flask_restful import Resource
import json
from flask import jsonify, request
from models.seller import Land


class PostLand(Resource):

    def post(self):
        data = json.loads(request.data)
        land = Land(city=data.get('city'),
                    district=data.get('district'),
                    land_area=data.get('land_area'),
                    number_street=data.get('number_street'),
                    block_number=data.get('block_number'),
                    )

        return land
