from typing import Dict, Any
import model.shopee as main_model
import view.shopee as main_view
import model.csv as csv_model
import view.csv as csv_view

def scrape(keyword: str, min_price: int, max_price: int, result_limit: int, output_file: str) -> Dict[str, Any]:
    ndjson = []
    for selenium_data in main_model.get_data(keyword, min_price, max_price, result_limit):
        ndjson.append(main_view.parse_raw_data(selenium_data))
    
    output_file = f"shopee:{output_file}"
    csv_model.to_csv(ndjson, output_file)
    return csv_view.to_response(len(ndjson), output_file)
