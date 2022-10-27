"""REST client handling, including atlassianScimStream base class."""

from typing import Any, Dict, Optional
from memoization import cached
from singer_sdk.streams import RESTStream
from singer_sdk.authenticators import BearerTokenAuthenticator
from tap_atlassian_scim.pagination import AtlassianScimPaginator

PAGINATION_INDEX = 1


class AtlassianScimStream(RESTStream):
    """atlassianScim stream class."""
    @property
    def url_base(self) -> str:
        """Return the API URL root, configurable via tap settings."""
        api_url = self.config['api_url']
        directory_id = self.config['directory_id']
        return f'{api_url}/scim/directory/{directory_id}'

    records_jsonpath = '$.Resources[*]'

    @property
    @cached
    def authenticator(self) -> BearerTokenAuthenticator:
        """Return a new authenticator object."""
        token = self.config['api_key']
        return BearerTokenAuthenticator.create_for_stream(self, token)

    @property
    def http_headers(self) -> dict:
        """Return the http headers needed."""
        headers = {'Accept': 'application/json'}

        if 'user_agent' in self.config:
            headers['User-Agent'] = self.config['user_agent']

        return headers

    def get_new_paginator(self) -> AtlassianScimPaginator:
        limit = self.config['limit']
        return AtlassianScimPaginator(start_value=PAGINATION_INDEX, page_size=limit)

    def get_url_params(
        self, context: Optional[dict], next_page_token: Optional[Any]
    ) -> Dict[str, Any]:
        """Return a dictionary of values to be used in URL parameterization."""
        params = {
            'startIndex': PAGINATION_INDEX,
            'count': self.config['limit']
        }
        
        if next_page_token:
            params['startIndex'] = next_page_token

        return params
