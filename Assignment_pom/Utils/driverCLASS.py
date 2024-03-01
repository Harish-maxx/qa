from selenium import webdriver
from Amazon_Automation.Pages.homePage import homePage
class BrowserDriver():

    def get_chrome_driver(self):
        # Initialize and return the driver
        driver = webdriver.Chrome()
        # Maximize the browser window
        driver.maximize_window()

        return driver

    def get_firefox_driver(self):
        # Initialize and return the driver
        driver = webdriver.Firefox()
        # Maximize the browser window
        driver.maximize_window()

        return driver

    def get_edge_driver(self):
        # Initialize and return the driver
        driver = webdriver.Edge()
        # Maximize the browser window
        driver.maximize_window()
        return driver

    def get_safari_driver(self):
        # Initialize and return the driver
        driver = webdriver.Safari()
        # Maximize the browser window
        driver.maximize_window()
        return driver