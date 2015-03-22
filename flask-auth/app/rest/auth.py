from flask.ext.httpauth import HTTPBasicAuth
from flask import g

from models import User
from app.rest import make_response, CODES

from datetime import datetime, timedelta
from time import sleep

import jwt

secret = "secret key"

auth = HTTPBasicAuth()
login = HTTPBasicAuth()


def get_session_token(payload, secret, expiration_time_secs=900):
    payload['exp'] = datetime.utcnow() + timedelta(seconds=expiration_time_secs)
    return jwt.encode(
        payload,
        secret,
        'HS512'
    )


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


@auth.error_handler
def auth_error():
    return make_response(None, CODES["ERROR_AUTH_REQUIRED"], 401)


@login.error_handler
def login_error():
    return make_response(None, CODES["ERROR_AUTH_REQUIRED"], 401)
