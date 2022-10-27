from singer_sdk.pagination import BaseOffsetPaginator
from requests import Response

class AtlassianScimPaginator(BaseOffsetPaginator):
    def has_more(self, response: Response) -> bool:
        fields = ['totalResults', 'startIndex', 'itemsPerPage']
        page = {k:v for k,v in response.json().items() if k in fields}
        start_index = page.get('startIndex', self._value)
        items_per_page = page.get('itemsPerPage', self._page_size)
        total_results = page.get('totalResults', 0)
        return start_index + items_per_page < total_results
