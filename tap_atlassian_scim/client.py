"""REST client handling, including atlassianScimStream base class."""

import requests
from typing import Any, Dict, Optional, Union, List, Iterable
from memoization import cached
from singer_sdk.streams import RESTStream
from singer_sdk.authenticators import BearerTokenAuthenticator

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
        return BearerTokenAuthenticator.create_for_stream(
            self,
            token=self.config.get('directory_api_key')
        )

    @property
    def http_headers(self) -> dict:
        """Return the http headers needed."""
        headers = {'Accept': 'application/json'}

        if 'user_agent' in self.config:
            headers['User-Agent'] = self.config.get('user_agent')

        return headers

    def get_next_page_token(
        self, response: requests.Response, previous_token: Optional[Any]
    ) -> Optional[Any]:
        """Return a token for identifying next page or None if no more pages."""
        # TODO: If pagination is required, return a token which can be used to get the
        #       next page. If this is the final page, return "None" to end the
        #       pagination loop.
        
        # if self.next_page_token_jsonpath:
        #     all_matches = extract_jsonpath(
     #            self.next_page_token_jsonpath, response.json()
        #     )
        #     first_match = next(iter(all_matches), None)
        #     next_page_token = first_match
        if previous_token: 
            if response.json().get("totalResults") < previous_token:
                return None 
            else:
                next_page_token = previous_token + self.config["batch_size"]
        else:
            next_page_token = 1 + self.config["batch_size"]
        return next_page_token

    def get_url_params(
        self, context: Optional[dict], next_page_token: Optional[Any]
    ) -> Dict[str, Any]:
        """Return a dictionary of values to be used in URL parameterization."""
        params: dict = {}
        if next_page_token:
            params["startIndex"] = next_page_token

        else: 
            params["startIndex"] = 1
            
        params["count"] = self.config["batch_size"]

        return params

