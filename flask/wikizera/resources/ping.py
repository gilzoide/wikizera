# -*- coding: utf-8 -*-

from flask_restful import Resource

class PingResource(Resource):
    def get(self):
        return "pong"

def setup(api):
    api.add_resource(PingResource, '/ping')
