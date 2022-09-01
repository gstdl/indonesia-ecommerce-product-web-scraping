from typing import List, Dict, Any
from datetime import datetime
import os
import csv

def to_csv(rows: List[Dict[str, Any]], filename: str):
    with open(os.path.join("../output", filename), "w") as f:
        writer = csv.DictWriter(f, ["product_name", "price", "product_category_l1", "product_category_l2", "product_category_l3", "processed_timestamp"])
        writer.writeheader()
        for row in rows:
            writer.writerow({"processed_timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"), **row})
