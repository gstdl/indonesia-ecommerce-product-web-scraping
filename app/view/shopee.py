from typing import Dict, Any
import json

from bs4 import BeautifulSoup

def parse_raw_data(selenium_data: Dict[str, Any]) -> Dict[str, Any]:
    html = BeautifulSoup(selenium_data["page_source"], "html.parser")
    res = {}
    
    # get product name
    name_div = html.find("div", class_="_2rQP1z")
    name = name_div.find("span").get_text()
    res["product_name"] = name
    
    # get product price
    price = html.find("div", class_="_2Shl1j").get_text()
    res["price"] = price
    
    # get product_category
    product_category = None
    scripts = html.find_all("script")
    for s in scripts:
        try:
            d = json.loads(s.get_text())
            if d["@type"] == "BreadcrumbList":
                product_category = [i["item"]["name"] for i in d["itemListElement"] if i["position"] < 5][1:]
            while len(res["product_category"]) < 3:
                product_category.append(None)
        except:
            pass
    if product_category:
        res["product_category_l1"] = product_category[0]
        res["product_category_l2"] = product_category[1]
        res["product_category_l3"] = product_category[2]
    return res
