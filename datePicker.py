import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()

try:

    driver.get("https://jqueryui.com/datepicker/")


    iframe = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "iframe")))
    driver.switch_to.frame(iframe)


    date_input = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "datepicker")))
    date_input.click()


    date_input.clear()


    date_input.send_keys("02/15/2023")
    time.sleep(2)

    date_input.send_keys(Keys.ENTER)


    selected_date = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//input[@id='datepicker'][@value='02/15/2024']")))
    print("Selected date:", selected_date.get_attribute("value"))

except Exception as e:
    print("An error occurred:", str(e))

finally:
    time.sleep(4)
    driver.quit()
