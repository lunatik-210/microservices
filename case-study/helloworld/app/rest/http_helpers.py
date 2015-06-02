import json

from flask import make_response as flask_make_response
from flask import Response

CODES = dict(
    OK=dict(
        code=0,
        description="OK"
    ),
    ERROR_SERVER_EXCEPTION=dict(
        code=1,
        description="Server exception during execution"
    ),
    ERROR_AUTH_REQUIRED=dict(
        code=2,
        description="Authorization required"
    ),
    ERROR_INVALID_REQUEST=dict(
        code=3,
        description="Invalid request"
    )
)


def add_cross_domain_headers(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'GET, POST, PUT, OPTIONS, DELETE'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type, Authorization'
    response.headers['Access-Control-Allow-Credentials'] = 'false'
    response.headers['Access-Control-Max-Age'] = '60'
    return response


def make_response(data, code, http_code=200):
    data = dict(
        error=dict(
            code=code.get('code'),
            http_code=http_code,
            description=code.get('description')
        ),
        result=data
    )
    response = flask_make_response(json.dumps(data, indent=4), http_code)
    response.headers['Content-Type'] = 'application/json; charset=utf-8'
    return add_cross_domain_headers(response)

def make_response_by_response(response):
    return Response(response=response.text, status=response.status_code, headers=response.headers.items())
