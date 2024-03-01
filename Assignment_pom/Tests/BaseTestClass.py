import logging
import unittest
import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from Assignment_pom.Utils.driverCLASS import BrowserDriver
from Assignment_pom.Pages.PageElements import pageElements
from Assignment_pom.Pages.loginElements import loginElements
from Assignment_pom.Tests.LoginPageActions import test_Login

class TestFarFetch(unittest.TestCase):

    def setUp(self):
        driver_cls = BrowserDriver()
        self.driver = driver_cls.get_chrome_driver()
        self.driver.maximize_window()
        le = loginElements(self.driver)
        self.driver.get(le.webUrl)
        time.sleep(2)

    def tearDown(self):
        self.driver.quit()

    def test_PerformOperations(self):
        p = pageElements(self.driver)
        """t = test_Login(self.driver)
        t.test_Logins()"""

        logging.basicConfig(filename='testResult.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, p.menswear_xpath))).click()
        logging.info('Clicked on menswear')
        time.sleep(2)

        shoes_element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, p.shoes_xpath)))
        ActionChains(self.driver).move_to_element(shoes_element).perform()
        self.driver.save_screenshot("shoes.png")
        time.sleep(2)
        self.driver.save_screenshot("pass.png")

        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, p.boots_xpath))).click()
        time.sleep(2)
        self.driver.save_screenshot("pass.png")

        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, p.filter_btn_xpath))).click()
        time.sleep(2)

        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, p.size_xpath))).click()
        time.sleep(2)

        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, p.country_drp_xpath))).click()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, p.brazil))).click()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, p.sizechart_xpath))).click()
        time.sleep(2)

        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, p.show_result_xpath))).click()
        time.sleep(2)

        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, p.sort_xpath))).click()
        time.sleep(2)

        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, p.ourpicks_xpath))).click()
        time.sleep(2)

        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, p.select_shoe_xpath))).click()
        time.sleep(2)

        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, p.size_guidexpath))).click()
        time.sleep(2)

        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, p.forty_xpath))).click()
        time.sleep(2)

        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, p.addToBag_xpath))).click()
        time.sleep(2)

        price = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, p.price_xpath)))
        logging.info(price.text)
        time.sleep(2)


if __name__ == '__main__':
    unittest.main()

