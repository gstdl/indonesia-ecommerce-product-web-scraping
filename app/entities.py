from pydantic import BaseModel, StrictStr, StrictInt, validator
from config.shopee import ShopeeSearchConfig

class BodyShopeeRequest(BaseModel):
    keyword: StrictStr
    result_limit: StrictInt = 60
    output_file: StrictStr
    min_price: StrictInt | None = None
    max_price: StrictInt | None = None
    
    @validator('keyword')
    def validate_keyword(cls, v):
        if v.strip() == '':
            raise ValueError(f"Invalid keyword (Empty string or spaces only are not allowed)")
        return v

    @validator('result_limit')
    def validate_result_limit(cls, v):
        """
        Note: shopee has search limit of 50 pages with 60 items per page (total 3000 items)
        """
        if v < 1 or v > ShopeeSearchConfig.MAX_ITEMS_PER_SEARCH:
            raise ValueError("result_limit must be between 1 and 3000")
        return v

    @validator('output_file')
    def check_output_file_extenstion(cls, v):
        if v.split(".")[-1] != "csv":
            raise ValueError("Expecting `csv` as output file extenstion")
        return v

    @validator('max_price')
    def max_price_higher_than_min_price(cls, v, values, **kwargs):
        if v is not None and values.get("min_price") is not None and v < values.get("min_price"):
            raise ValueError('Value of `max_price` must be higher than `min_price`')
        return v

class DefaultResponse(BaseModel):
    message: str
    output_file: str
    number_of_rows_written: int
