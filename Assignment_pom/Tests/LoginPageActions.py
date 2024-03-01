import unittest
import logging
import unittest

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from Assignment_pom.Utils.driverCLASS import BrowserDriver
from Assignment_pom.Pages.PageElements import pageElements
from Assignment_pom.Pages.loginElements import loginElements
from Assignment_pom.Pages.loginValues import loginValues

class test_Login(unittest.TestCase):

    def setUp(self):
        driverCls = BrowserDriver()
        self.driver = driverCls.get_chrome_driver()
        self.driver.maximize_window()
        le = loginElements(self.driver)
        self.driver.get(le.webUrl)
        time.sleep(2)

    def test_Logins(self):
        le = loginElements(self.driver)
        lv = loginValues(self.driver)
        time.sleep(2)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, le.signin_xpath))).click()
        time.sleep(2)

        """Send Keys to username field"""
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, le.username_xpath))).send_keys(
            lv.username)
        time.sleep(3)

        """Send Keys to pass field"""
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, le.password_xpath))).send_keys(
            lv.password)
        time.sleep(3)

        """Click on signin"""
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, le.signin_btn_xpath))).click()
        time.sleep(3)

    def tearDown(self):
        self.driver.quit()

        
