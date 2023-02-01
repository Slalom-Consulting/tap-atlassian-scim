"""Pagination handling for AtlassianScimStream."""

from requests import Response
from singer_sdk.pagination import BaseOffsetPaginator


class AtlassianScimPaginator(BaseOffsetPaginator):
    def has_more(self, response: Response) -> bool:
        total_results = response.json().get("totalResults", 0)
        return self.get_next(response) < total_results
