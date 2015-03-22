from flask import current_app

from app import db
from app.rest import get_session_token

from jwt import decode
from jwt.exceptions import ExpiredSignatureError

from passlib.apps import custom_app_context as pwd_context


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
        token = get_session_token(dict(user=user, is_refresh=False), app.config['SECRET_KEY'])
        refresh_token = get_session_token(dict(user=user, is_refresh=True), app.config['SECRET_KEY'], 172800)
        return token, refresh_token

    @staticmethod
    def verify_auth_token(token):
        app = current_app._get_current_object()
        try:
            data = decode(token, app.config['SECRET_KEY'])
        #valid token, but expired
        except ExpiredSignatureError:
            return None
        user = User.query.get(data['user']['id'])
        return user

    @staticmethod
    def get_user_by_id(user_id):
        return User.query.filter(User.id == user_id).first()
