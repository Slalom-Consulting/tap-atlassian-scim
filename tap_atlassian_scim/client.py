"""REST client handling, including atlassianScimStream base class."""

from typing import Any, Dict, Optional
from urllib.parse import urljoin

from singer_sdk.authenticators import BearerTokenAuthenticator
from singer_sdk.streams import RESTStream

from tap_atlassian_scim.pagination import AtlassianScimPaginator

PAGINATION_INDEX = 1
API_URL = "https://api.atlassian.com"


class AtlassianScimStream(RESTStream):
    """atlassianScim stream class."""

    records_jsonpath = "$.Resources[*]"

    @property
    def url_base(self) -> str:
        base = self.config.get("api_url", API_URL)
        endpoint = "/scim/directory/{directory_id}"
        return urljoin(base, endpoint)

    @property
    def authenticator(self) -> BearerTokenAuthenticator:
        token = str(self.config["api_key"])
        return BearerTokenAuthenticator(self, token)

    @property
    def http_headers(self) -> dict:
        headers = {"Accept": "application/json"}

        if self.config.get("user_agent"):
            headers["User-Agent"] = str(self.config["user_agent"])

        return headers

    def get_new_paginator(self) -> AtlassianScimPaginator:
        limit = int(self.config["limit"])
        return AtlassianScimPaginator(start_value=PAGINATION_INDEX, page_size=limit)

    def get_url_params(
        self, context: Optional[dict], next_page_token: Optional[Any]
    ) -> Dict[str, Any]:
        return {
            "startIndex": next_page_token or PAGINATION_INDEX,
            "count": self.config.get("limit"),
        }
