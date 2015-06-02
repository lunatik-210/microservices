import traceback

from flask import request
from flask.ext.restful import Resource

from app.rest.http_helpers import make_response, make_response_by_response, CODES

import requests


class HelloWorldResource(Resource):
    def options(self):
        try:
            return make_response(None, CODES["OK"], 200)
        except Exception:
            print traceback.print_exc()
            return make_response(None, CODES["ERROR_SERVER_EXCEPTION"], 400)

    def get(self):
        try:
            response = requests.get('http://localhost:5002/v1/helloworld', params=request.args, headers=request.headers)
            return make_response_by_response(response)
        except Exception:
            print traceback.print_exc()
            return make_response(None, CODES["ERROR_SERVER_EXCEPTION"], 400)
