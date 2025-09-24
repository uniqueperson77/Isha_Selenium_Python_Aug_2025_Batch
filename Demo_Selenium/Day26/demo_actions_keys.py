import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://demo.automationtesting.in/Register.html")
time.sleep(5)

action_obj = ActionChains(driver)
action_obj.key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).perform()

time.sleep(5)

driver.close()






