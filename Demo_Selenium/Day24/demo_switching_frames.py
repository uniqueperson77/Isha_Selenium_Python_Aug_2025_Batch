from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://demo.automationtesting.in/Frames.html")
driver.maximize_window()
time.sleep(5)

# driver.switch_to.frame("SingleFrame")       #name as attrib

web_element = driver.find_element(By.ID,"singleframe")
driver.switch_to.frame(web_element)

driver.find_element(By.TAG_NAME,"input").send_keys("Hello World....")

time.sleep(3)

driver.switch_to.default_content()

driver.find_element(By.LINK_TEXT,"Register").click()

driver.quit()