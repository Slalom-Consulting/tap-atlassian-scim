from singer_sdk.pagination import BaseOffsetPaginator
from requests import Response


class AtlassianScimPaginator(BaseOffsetPaginator):
    def has_more(self, response: Response) -> bool:
        total_results = response.json().get('totalResults', 0)
        return self.get_next() < total_results
