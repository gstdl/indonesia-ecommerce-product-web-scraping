import os
import yaml
from config import SearchConfig, SeleniumChromeConfig

CURRENT_WORKING_DIRECTORY = os.getcwd()
ENV = os.environ.get("ENV")
if ENV is None:
    ENV = "development"
config_file_path = os.path.join(CURRENT_WORKING_DIRECTORY, "config", ENV, "shopee.yaml")

with open(config_file_path, "r") as config_file:
    shopee_config = yaml.safe_load(config_file)

ShopeeSearchConfig = SearchConfig(**(shopee_config["search"]))

ShopeeSeleniumConfig = SeleniumChromeConfig()
