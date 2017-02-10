# -*- coding: utf-8 -*-

from flask_restful import Resource
from flask_security import auth_token_required, current_user

class UserResource(Resource):
    @auth_token_required
    def get(self):
        return {
            'user': {
                'username': current_user.username,
                'email': current_user.email,
                'authtoken': current_user.get_auth_token(),
            }
        }

def setup(api):
    api.add_resource(UserResource, '/user')
