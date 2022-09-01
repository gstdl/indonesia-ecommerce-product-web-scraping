from fastapi import FastAPI
import entities
import controller.shopee

app = FastAPI()

@app.post("/shopee", response_model=entities.DefaultResponse, name="Scraper", tags=["shopee"], description="endpoint to scrape shopee product data and store it to CSV")
def scrape_shopee_data_to_csv(body: entities.BodyShopeeRequest) -> entities.DefaultResponse:
    result = controller.shopee.scrape(
        keyword=body.keyword,
        min_price=body.min_price,
        max_price=body.max_price,
        result_limit=body.result_limit,
        output_file=body.output_file,
    )
    return result
