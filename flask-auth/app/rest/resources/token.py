import traceback

from flask import g
from flask.ext.restful import Resource

from app.rest.http_helpers import make_response, CODES

from app.rest import login


class TokenResource(Resource):
    def options(self):
        try:
            return make_response(None, CODES["OK"], 200)
        except Exception:
            print traceback.print_exc()
            return make_response(None, CODES["ERROR_SERVER_EXCEPTION"], 400)

    @login.login_required
    def get(self):
        try:
            token, refresh_token = g.user.generate_auth_token()
            return make_response(dict(token=token, refresh_token=refresh_token), CODES["OK"], 201)
        except Exception:
            print traceback.print_exc()
            return make_response(None, CODES["ERROR_SERVER_EXCEPTION"], 400)


class RefreshTokenResource(Resource):
    def options(self):
        try:
            return make_response(None, CODES["OK"], 200)
        except Exception:
            print traceback.print_exc()
            return make_response(None, CODES["ERROR_SERVER_EXCEPTION"], 400)

    def get(self):
        try:
            return make_response("", CODES["OK"], 201)
        except Exception:
            print traceback.print_exc()
            return make_response(None, CODES["ERROR_SERVER_EXCEPTION"], 400)
