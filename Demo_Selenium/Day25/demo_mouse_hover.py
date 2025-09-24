import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://demo.automationtesting.in/Register.html")
time.sleep(5)


#mouse hover on the web-element
xpath_for_switch_to_element = "//a[text()='SwitchTo']"
switch_to_web_element = driver.find_element(By.XPATH,xpath_for_switch_to_element)

action_obj = ActionChains(driver)
action_obj.move_to_element(switch_to_web_element).perform()

time.sleep(5)

driver.find_element(By.LINK_TEXT,"Windows").click()


time.sleep(5)
