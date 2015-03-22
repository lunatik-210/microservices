from flask.ext.restful import reqparse
from flask import request
import urllib
import urlparse


def update_url(url, params):
    url_parts = list(urlparse.urlparse(url))
    query = dict(urlparse.parse_qsl(url_parts[4]))
    query.update(params)
    url_parts[4] = urllib.urlencode(query)
    return urlparse.urlunparse(url_parts)


class PaginationMixin():
    def __init__(self, default_page=1, default_size=10):
        self.default_page = default_page
        self.default_size = default_size
        self.get_parser = reqparse.RequestParser()
        self.get_parser.add_argument('page', type=int, default=default_page)
        self.get_parser.add_argument('size', type=int, default=default_size)

    def get_paging(self):
        args = self.get_parser.parse_args()
        if args.size < 0:
            args.size = self.default_size

        if args.page < 0:
            args.page = self.default_page

        return args

    def wrap_paging(self, data, paginator):
        args = self.get_paging()

        return dict(
            data=data,
            paging=dict(
                current=paginator.page,
                next=paginator.next_num if paginator.has_next else None,
                previous=paginator.prev_num if paginator.has_prev else None,
                total_items=paginator.total,
                total_pages=paginator.pages
            ),
            links=[
                dict(
                    href=update_url(request.url, dict(page=args.page+1, size=args.size)) if paginator.has_next else None,
                    method="GET",
                    rel="next_page"
                ),
                dict(
                    href=update_url(request.url, dict(page=args.page-1, size=args.size)) if paginator.has_prev else None,
                    method="GET",
                    rel="prev_page"
                ),
                dict(
                    href=request.base_url,
                    method="GET",
                    rel="self"
                )
            ]
        )
