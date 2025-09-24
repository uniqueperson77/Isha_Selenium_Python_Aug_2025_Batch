import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.abhibus.com/")
# time.sleep(5)

driver.implicitly_wait(5)           #5/0.5  = 10

# driver.find_element(By.XPATH,"//a//span[text()='Search']").click()

driver.find_element(By.XPATH,"//a//span[text()='Hotels']").click()

driver.find_element(By.XPATH,"//a//p[text()='Customer Service']").click()

time.sleep(5)