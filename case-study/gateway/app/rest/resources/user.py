# -*- coding: utf-8 -*-
import traceback

from flask import request, current_app
from flask.ext.restful import Resource

from app.rest import make_response, make_response_by_response, CODES

import requests

class UserResource(Resource):
    def options(self, id):
        try:
            return make_response(None, CODES["OK"], 200)
        except Exception:
            print traceback.print_exc()
            return make_response(None, CODES["ERROR_SERVER_EXCEPTION"], 400)

    def get(self, id):
        try:
            app = current_app._get_current_object()
            response = requests.get(app.config['AUTH_SERVICE']+'/v1/users/'+id, headers=request.headers)
            return make_response_by_response(response)
        except Exception:
            print traceback.print_exc()
            return make_response(None, CODES["ERROR_SERVER_EXCEPTION"], 400)

    def delete(self, id):
        try:
            app = current_app._get_current_object()
            response = requests.delete(app.config['AUTH_SERVICE']+'/v1/users/'+id, headers=request.headers)
            return make_response_by_response(response)
        except Exception:
            print traceback.print_exc()
            return make_response(None, CODES["ERROR_SERVER_EXCEPTION"], 400)


class UsersResource(Resource):
    def options(self):
        try:
            return make_response(None, CODES["OK"], 200)
        except Exception:
            print traceback.print_exc()
            return make_response(None, CODES["ERROR_SERVER_EXCEPTION"], 400)
    
    def get(self):
        try:
            app = current_app._get_current_object()
            response = requests.get(app.config['AUTH_SERVICE']+'/v1/users', headers=request.headers)
            return make_response_by_response(response)
        except Exception:
            print traceback.print_exc()
            return make_response(None, CODES["ERROR_SERVER_EXCEPTION"], 400)

    def post(self):
        try:
            app = current_app._get_current_object()
            response = requests.post(app.config['AUTH_SERVICE']+'/v1/users', data=request.json)
            return make_response_by_response(response)
        except Exception:
            print traceback.print_exc()
            return make_response(None, CODES["ERROR_SERVER_EXCEPTION"], 400)
