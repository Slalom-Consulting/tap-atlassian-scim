"""REST client handling, including atlassianScimStream base class."""

import requests
from pathlib import Path
from typing import Any, Dict, Optional, Union, List, Iterable

from memoization import cached

from singer_sdk.helpers.jsonpath import extract_jsonpath
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

    records_jsonpath = "$.Resources[*]"  # Or override `parse_response`.
    # next_page_token_jsonpath = "$.next_page"  # Or override `get_next_page_token`.

    @property
    def authenticator(self) -> BearerTokenAuthenticator:
        """Return a new authenticator object."""
        return BearerTokenAuthenticator.create_for_stream(
            self,
            token=self.config.get("directory_api_key")
        )

    @property
    def http_headers(self) -> dict:
        """Return the http headers needed."""
        headers = {"Accept": "application/json"}
        if "user_agent" in self.config:
            headers["User-Agent"] = self.config.get("user_agent")
        # If not using an authenticator, you may also provide inline auth headers:
        # headers["Private-Token"] = self.config.get("auth_token")
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

        # if self.replication_key:
        #    params["sort"] = "asc"
        #    params["order_by"] = self.replication_key
        return params

    def prepare_request_payload(
        self, context: Optional[dict], next_page_token: Optional[Any]
    ) -> Optional[dict]:
        """Prepare the data payload for the REST API request.

        By default, no payload will be sent (return None).
        """
        # TODO: Delete this method if no payload is required. (Most REST APIs.)
        return None

    def parse_response(self, response: requests.Response) -> Iterable[dict]:
        """Parse the response and return an iterator of result rows."""
        # TODO: Parse response body and return a set of records.
        yield from extract_jsonpath(self.records_jsonpath, input=response.json())

    def post_process(self, row: dict, context: Optional[dict]) -> dict:
        """As needed, append or transform raw data to match expected structure."""
        # TODO: Delete this method if not needed.
        return row
