from selenium import webdriver

class Selenium:
    def __init__(self, config):
        self.config = config

    def __enter__(self):
        self.driver = webdriver.Chrome(executable_path=self.config.EXECUTABLE_PATH)
        return self.driver

    def __exit__(self, exc_type, exc_value, trace):
        self.driver.close()
        del self.driver
