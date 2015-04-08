from flask.ext.httpauth import HTTPBasicAuth
from flask import g

from app.models import User
from app.rest import make_response, CODES

from datetime import datetime, timedelta

auth = HTTPBasicAuth()
login = HTTPBasicAuth()
refresh = HTTPBasicAuth()


@login.verify_password
def verify_password(email, password):
    user = User.query.filter_by(email=email).first()
    if not user or not user.verify_password(password):
        return False
    g.user = user
    return True


@auth.verify_password
def verify_token(token, passw=None):
    user = User.verify_auth_token(token)
    if not user:
        return False
    g.user = user
    return True


@refresh.verify_password
def refresh_token(token, refresh_token):    
    user = User.verify_refresh_token(token, refresh_token)
    if not user:
        return False
    g.user = user
    return True


@auth.error_handler
def auth_error():
    if g.error == "ExpiredSignatureError":
        return make_response(None, CODES["ERROR_SESSION_EXPIRED"], 400)
    return make_response(None, CODES["ERROR_AUTH_REQUIRED"], 401)


@login.error_handler
def login_error():
    return make_response(None, CODES["ERROR_AUTH_REQUIRED"], 401)


@refresh.error_handler
def refresh_error():
    return make_response(None, CODES["ERROR_INVALID_REQUEST"], 400)