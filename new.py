from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()
time.sleep(5)
print(driver.title)

user1 = driver.find_element(By.XPATH,"//div[@class='oxd-sheet oxd-sheet--rounded oxd-sheet--gutters oxd-sheet--gray-lighten-2 orangehrm-demo-credentials']/p[1]")
pass1 = driver.find_element(By.XPATH,"//div[@class='oxd-sheet oxd-sheet--rounded oxd-sheet--gutters oxd-sheet--gray-lighten-2 orangehrm-demo-credentials']/p[2]")

userRes = user1.text
passRes = pass1.text
print(userRes +"\n"+ passRes)

userString = userRes.split(":")
s = userString[1].strip()
print(s)


passString = passRes.split(":")
p = passString[1].strip()
print(p)

driver.find_element(By.XPATH,"//input[@name='username']").send_keys(s)
driver.find_element(By.NAME,"password").send_keys(p)
driver.find_element(By.XPATH,"//button[@type='submit']").click()
print("Test case Passed")
