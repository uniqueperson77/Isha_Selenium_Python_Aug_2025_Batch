import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select



driver = webdriver.Chrome()
driver.set_page_load_timeout(5)
driver.get("https://demo.automationtesting.in/Register.html")
driver.implicitly_wait(10)
# time.sleep(10)
# time.sleep(5)
driver.find_element(By.XPATH,"//input[@ng-model='FirstName']").send_keys("Ishaaa.....")
driver.find_element(By.XPATH,"//input[@ng-model='LastName']").send_keys("Ishaaa.....")

# insta = Select(driver.find_element(By.ID,"Skills"))
# insta.select_by_value("Android")
# print(insta.options)
# for ele in insta.options:
#     print(ele.text)


time.sleep(5)       # this will pause the execution