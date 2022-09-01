from typing import Iterator
from math import ceil

from pydantic import BaseModel, StrictStr, StrictInt

class SearchConfig(BaseModel):
    SEARCH_URL: StrictStr
    MAX_PAGES: StrictInt
    ITEMS_PER_PAGE: StrictInt
    
    class Config:
        allow_mutation = False

    @property
    def MAX_ITEMS_PER_SEARCH(self) -> int:
        return self.MAX_PAGES * self.ITEMS_PER_PAGE

    def get_page_range_zero_indexed(self, result_limit) -> Iterator[int]:
        page_limit = ceil(result_limit / self.ITEMS_PER_PAGE)
        return range(page_limit)

class SeleniumChromeConfig(BaseModel):
    EXECUTABLE_PATH: StrictStr = "/usr/local/bin/chromedriver"
    
    class Config:
        allow_mutation = False