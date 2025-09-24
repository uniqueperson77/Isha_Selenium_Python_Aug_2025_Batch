import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://demo.automationtesting.in/Register.html")
time.sleep(5)

web_element = driver.find_element(By.ID,"firstpassword")

print(web_element.get_attribute("type"))
print(web_element.get_attribute("ng-model"))


exit()

#getting title of web page
webpage_title = driver.title

print(webpage_title)

#getting current url of web page
print(driver.current_url)

driver.find_element(By.LINK_TEXT,"WebTable").click()

webpage_title = driver.title

print(webpage_title)

print(driver.current_url)

exit()











driver.find_element(By.LINK_TEXT,"WebTable").click()

time.sleep(5)

### step back

driver.back()

time.sleep(2.5)

# step forward

driver.forward()

time.sleep(5)
