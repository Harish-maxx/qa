import time

import ExcelUtil
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/login")
driver.maximize_window()
time.sleep(5)

path = "C://Users//harip//PycharmProjects//qa//dataFile.xlsx"

rows = ExcelUtil.getRowCount(path, 'Sheet1')

for r in range(2, rows+1):
    username = ExcelUtil.readExcel(path,"Sheet1",r,1)
    password = ExcelUtil.readExcel(path,"Sheet1",r,2)


    driver.find_element(By.ID, "username").send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.XPATH, "//*[@id='login']/button/i").click()

    if driver.title == 'The Internet':
        print("Login is successful")
        ExcelUtil.writeData(path,"Sheet1",r,3,"Test Passed")
    else:
        print("Login is Failed")
        ExcelUtil.writeData(path, "Sheet1", r, 3, "Test Failed")

    driver.find_element(By.XPATH, "//*[@id='content']/div/a/i").click()












#total_rows = sheetName.max_row
#total_col = sheetName.max_column
#print(sheetName.cell(1,2).value)


#for r in range(1,total_rows+1):
 #   for c in range(1,total_col+1):
  #      print(sheetName.cell(r,c).value, end= " ")
  #  print()
