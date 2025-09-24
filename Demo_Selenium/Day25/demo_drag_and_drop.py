import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://demo.automationtesting.in/Register.html")
time.sleep(5)
obj = ActionChains(driver)

#mouse hover on the web-element
xpath_for_interactions_element = "//a[text()='Interactions ']"
interactions_web_element = driver.find_element(By.XPATH,xpath_for_interactions_element)
obj.move_to_element(interactions_web_element).perform()

#mouse hover on the web-element
xpath_for_element = "//a[text()='Drag and Drop ']"
web_element = driver.find_element(By.XPATH,xpath_for_element)
obj.move_to_element(web_element).perform()

time.sleep(3)

driver.find_element(By.PARTIAL_LINK_TEXT,"Static").click()


time.sleep(5)


#####################  drag & drop
source = driver.find_element(By.ID,"node")
source1 = driver.find_element(By.ID,"mongo")
target = driver.find_element(By.ID,"droparea")

obj.drag_and_drop(source,target).perform()
time.sleep(2)
obj.drag_and_drop(source1,target).perform()

time.sleep(5)
