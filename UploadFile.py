from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/upload")
driver.maximize_window()
time.sleep(5)

driver.find_element(By.ID, "file-upload").send_keys("C://Users//harip//Downloads//Book1.xlsx")
time.sleep(5)

driver.find_element(By.ID, "file-submit").click()
try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "h3"))
    )
finally:
    print("passed")