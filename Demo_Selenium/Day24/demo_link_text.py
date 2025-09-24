from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://demo.automationtesting.in/Register.html")
time.sleep(3)
# web_element = driver.find_element(By.LINK_TEXT,"WebTable")
web_element = driver.find_element(By.PARTIAL_LINK_TEXT,"WebTab")
web_element.click()

time.sleep(5)
