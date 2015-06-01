from flask import current_app, g

from app import db

from jwt import decode, encode
from jwt.exceptions import ExpiredSignatureError, DecodeError

from passlib.apps import custom_app_context as pwd_context

from datetime import datetime, timedelta


def get_session_token(payload, secret, expiration_time_secs=900):
    payload['exp'] = datetime.utcnow() + timedelta(seconds=expiration_time_secs)
    return encode(payload, secret, 'HS512')


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(250), nullable=False, unique=True)
    encrypted_password = db.Column(db.String(250), nullable=False)

    def encrypt_password(self, password):
        self.encrypted_password = pwd_context.encrypt(password)

    def verify_password(self, password):
        return pwd_context.verify(password, self.encrypted_password)

    def generate_auth_token(self):
        app = current_app._get_current_object()
        user = dict(id=self.id, email=self.email)
        token = get_session_token(dict(user=user, is_refresh=False), app.config['SECRET_KEY'], 1200)
        refresh_token = get_session_token(dict(user=user, is_refresh=True), app.config['SECRET_KEY'], 172800)
        return token, refresh_token

    @staticmethod
    def verify_refresh_token(token, refresh_token):
        app = current_app._get_current_object()
        if token and refresh_token:
            try:
                d_token = decode(token, app.config['SECRET_KEY'])
            except ExpiredSignatureError:
                pass
            except DecodeError:
                return None
            
            try:
                d_refresh_token = decode(refresh_token, app.config['SECRET_KEY'])
            except ExpiredSignatureError:
                return None
            except DecodeError:
                return None
        else:
            return None

        user = User.query.get(d_refresh_token['user']['id'])
        return user

    @staticmethod
    def verify_auth_token(token):
        app = current_app._get_current_object()
        try:
            data = decode(token, app.config['SECRET_KEY'])
        except ExpiredSignatureError:
            g.error = 'ExpiredSignatureError'
            return None
        except DecodeError:
            g.error = 'DecodeError'
            return None
        user = User.query.get(data['user']['id'])
        return user

    @staticmethod
    def get_user_by_id(user_id):
        return User.query.filter(User.id == user_id).first()
