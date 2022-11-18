"""REST client handling, including atlassianScimStream base class."""

from typing import Any, Dict, Optional
from memoization import cached
from singer_sdk.streams import RESTStream
from singer_sdk.authenticators import BearerTokenAuthenticator
from tap_atlassian_scim.pagination import AtlassianScimPaginator
from urllib.parse import urljoin

PAGINATION_INDEX = 1
API_URL = 'https://api.atlassian.com'


class AtlassianScimStream(RESTStream):
    """atlassianScim stream class."""
    records_jsonpath = '$.Resources[*]'

    @property
    def url_base(self) -> str:
        base = self.config.get('api_url', API_URL)
        endpoint = '/scim/directory/{directory_id}'
        return urljoin(base, endpoint)

    @property
    @cached
    def authenticator(self) -> BearerTokenAuthenticator:
        token = self.config.get('api_key')
        return BearerTokenAuthenticator(self, token)

    @property
    def http_headers(self) -> dict:
        headers = {'Accept': 'application/json'}

        if self.config.get('user_agent'):
            headers['User-Agent'] = self.config.get('user_agent')

        return headers

    def get_new_paginator(self) -> AtlassianScimPaginator:
        limit = self.config.get('limit')
        return AtlassianScimPaginator(start_value=PAGINATION_INDEX, page_size=limit)

    def get_url_params(
        self, context: Optional[dict], next_page_token: Optional[Any]
    ) -> Dict[str, Any]:
        return {
            'startIndex': next_page_token or PAGINATION_INDEX,
            'count': self.config.get('limit')
        }   

