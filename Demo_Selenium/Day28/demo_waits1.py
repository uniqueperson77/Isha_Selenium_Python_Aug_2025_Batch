import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.set_page_load_timeout(5)
driver.get("https://demo.automationtesting.in/Register.html")

driver.find_element(By.XPATH,"//input[@ng-model='FirstName']").send_keys("Ishaaa.....")


time.sleep(5)