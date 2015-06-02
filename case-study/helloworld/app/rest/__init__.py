from flask.ext import restful
from http_helpers import make_response, make_response_by_response, CODES

restv1 = restful.Api(prefix="/v1")

from . import urls
