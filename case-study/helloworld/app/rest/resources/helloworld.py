import traceback

from flask import request, current_app
from flask.ext.restful import Resource, reqparse

from app.rest.http_helpers import make_response, make_response_by_response, CODES

import requests

class HelloWorldResource(Resource):
    def __init__(self):
        self.get_parser = reqparse.RequestParser()
        self.get_parser.add_argument('x', type=int, required=True)
        self.get_parser.add_argument('y', type=int, required=True)

    def options(self):
        try:
            return make_response(None, CODES["OK"], 200)
        except Exception:
            print traceback.print_exc()
            return make_response(None, CODES["ERROR_SERVER_EXCEPTION"], 400)

    def get(self):
        try:
            app = current_app._get_current_object()
            response = requests.get(app.config['AUTH_SERVICE']+'/v1/authorize', headers=request.headers)
            if response.status_code != 200:
                return make_response_by_response(response)

            args = self.get_parser.parse_args()
            return make_response(args.x + args.y, CODES["OK"], 200)
        except Exception:
            print traceback.print_exc()
            return make_response(None, CODES["ERROR_SERVER_EXCEPTION"], 400)
