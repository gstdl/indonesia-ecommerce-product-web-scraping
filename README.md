## About this repostiory

This repository contains a web API to scrape product data from e-commerce.

## About the folders

The repository consist of 3 folders which are as follows:

- `app` (folder containing the main app)
- `output` (folder containing the (sample) output after invoking the web API)
- `docs` (supporting docs for documentation)

## Application design

The application follows the MVC software architecture. 
The app has subdirectories supporting the software architecture.

- `model` is where tha app interacts with external services such as selenium (web broswer) and local files.
- `view` is where data is parsed either for serving the app or parsing the data received from the models.
- `controller` is where all the logic flow is controlled.

In order to understand the flow in the application, check the image below.

![](docs/img/sequence%20diagram%20e-commerce%20scrapper.png)

## Requirments to run the app

1. Have python and Google Chrome installed in your machine
2. Install selenium according to your [Google Chrome version](https://chromedriver.storage.googleapis.com/index.html)
3. Install the python dependencies in [requirements.txt](requirements.txt)

## Running the app

### In development (debug) mode

```sh
$ cd app
$ uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

### In production

```sh
$ cd app
$ uvicorn main:app --host 0.0.0.0 --port 8000
```

After executing the command above, the app will be served on `localhost:8000`.

## Scraping

In order to scrape e-commerce, you need to invoke an API.
At the time of writing, you can only scrape shopee's product data.

---
note: full documentation of the app is served on `localhost:8000/docs` when the app is running

---

### Shopee

request url: `localhost:8000/shopee`
request method: `POST`
request body sample:
```json
{
    "keyword": "smartwatch",
    "output_file": "smartwatch_murah_10.csv",
    "result_limit": 10,
    "min_price": 10000,
    "max_price": 300000
}
```
