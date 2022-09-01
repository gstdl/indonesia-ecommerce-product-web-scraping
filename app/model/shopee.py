from typing import Iterator, Dict, Any
from urllib.parse import quote
import time

from config.shopee import ShopeeSearchConfig, ShopeeSeleniumConfig
from model.context_managers.selenium_lib import Selenium

from selenium.webdriver.common.by import By

def get_data(keyword: str, min_price: str, max_price: str, result_limit: str) -> Iterator[Dict[str, Any]]:
    search_url = ShopeeSearchConfig.SEARCH_URL
    params = {"keyword": quote(keyword)}
    if min_price or max_price:
        params.update({"noCorrection":"true"})
    if min_price:
        params.update({"minPrice": min_price})
    if max_price:
        params.update({"maxPrice": max_price})
    page_range = ShopeeSearchConfig.get_page_range_zero_indexed(result_limit)
    
    res_count = 0
    for page_number in page_range:
        params.update({"page":f"{page_number}"})
        url = search_url + "?" + "&".join([f"{k}={v}" for k,v in params.items()])
        with Selenium(ShopeeSeleniumConfig) as driver:
            driver.get(url)
            time.sleep(15)
            products = driver.find_elements(By.CLASS_NAME, 'shopee-search-item-result__item')
            for page in products:
                a = page.find_element(By.TAG_NAME, 'a')
                href = a.get_attribute('href')
                driver.execute_script(f"window.open('{href}', '_blank')")
                driver.switch_to.window(driver.window_handles[-1])
                time.sleep(15)
                yield {
                    "page_source": driver.page_source,
                    # "product_page_url": href,
                }
                res_count += 1
                if res_count == result_limit:
                    return
                driver.close()
                driver.switch_to.window(driver.window_handles[0])
