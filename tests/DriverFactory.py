from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


class DriverFactory:
    driver = None

    def create_driver(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

    def getDriver(self):
        return self.driver
