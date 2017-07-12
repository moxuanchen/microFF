# -*- coding: utf-8 -*-

from flask_restful import Api
from flask_restful import Resource

api = Api(prefix='/api')


class Login(Resource):
    def post(self):
        pass


api.add_resource(Login, '/user/login')
