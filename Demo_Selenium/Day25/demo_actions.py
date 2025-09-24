import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://demo.automationtesting.in/Register.html")
time.sleep(5)
obj = ActionChains(driver)

# #context click
# obj.context_click(driver.find_element(By.ID,"checkbox1")).perform()

# #double click
# obj.double_click(driver.find_element(By.ID,"checkbox1")).perform()

locator = "input[type='tel']"
web_ele = driver.find_element(By.CSS_SELECTOR,locator)
web_ele.send_keys("596184")
time.sleep(2)
web_ele.clear()
time.sleep(2)
obj.send_keys_to_element(web_ele,"100000").perform()
time.sleep(5)