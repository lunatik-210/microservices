# -*- coding: utf-8 -*-

import traceback

from flask import g
from flask.ext.restful import Resource
from app import db

from app.models import User

from app.rest import make_response, CODES
from app.rest import PaginationMixin

from flask.ext.restful import reqparse


class UserResource(Resource):
    def options(self, id):
        try:
            return make_response(None, CODES["OK"], 200)
        except Exception:
            print traceback.print_exc()
            return make_response(None, CODES["ERROR_SERVER_EXCEPTION"], 400)

    def get(self, id):
        try:
            user = User.query.filter_by(id=id).first()

            if user is None:
                return make_response(None, CODES["ERROR_INVALID_REQUEST"], 400)

            return make_response(dict(id=user.id, email=user.email), CODES["OK"], 200)
        except Exception:
            print traceback.print_exc()
            return make_response(None, CODES["ERROR_SERVER_EXCEPTION"], 400)

    def delete(self, id):
        try:
            user = User.query.filter_by(id=id).first()

            if user is None:
                return make_response(None, CODES["ERROR_INVALID_REQUEST"], 400)

            db.session.delete(user)
            db.session.commit()         

            return make_response(None, CODES["OK"], 200)
        except Exception:
            print traceback.print_exc()
            return make_response(None, CODES["ERROR_SERVER_EXCEPTION"], 400)


class UsersResource(Resource, PaginationMixin):
    def __init__(self):
        PaginationMixin.__init__(self)

        self.post_parser = reqparse.RequestParser()
        self.post_parser.add_argument('email', type=str, required=True)
        self.post_parser.add_argument('password', type=str, required=True)

    def options(self):
        try:
            return make_response(None, CODES["OK"], 200)
        except Exception:
            print traceback.print_exc()
            return make_response(None, CODES["ERROR_SERVER_EXCEPTION"], 400)
    
    def get(self):
        try:
            paging_args = self.get_paging()
            pagination = User.query.paginate(paging_args.page, per_page=paging_args.size, error_out=False)

            users = []
            for u in pagination.items:
                users.append(dict(id=u.id, email=u.email))
            data = self.wrap_paging(users, pagination)
            return make_response(data, CODES["OK"], 200)
        except Exception:
            print traceback.print_exc()
            return make_response(None, CODES["ERROR_SERVER_EXCEPTION"], 400)

    def post(self):
        try:
            args = self.post_parser.parse_args()

            if User.query.filter_by(email=args.email).first() is not None:
                return make_response(None, CODES["ERROR_INVALID_REQUEST"], 400)

            new_user = User()
            new_user.email = args.email
            new_user.encrypt_password(args.password)
            db.session.add(new_user)
            db.session.commit()

            return make_response(None, CODES["OK"], 201)
        except Exception:
            print traceback.print_exc()
            return make_response(None, CODES["ERROR_SERVER_EXCEPTION"], 400)
