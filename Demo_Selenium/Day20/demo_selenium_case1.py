import time
from selenium import webdriver
from selenium.webdriver.common.by import By

print("Launching the Chrome browser")
browser = webdriver.Chrome()        # launch the browser
time.sleep(2.5)

print("maximizing the window size")
browser.maximize_window()           #maximize window
# browser.minimize_window()

browser.get("https://demo.automationtesting.in/Register.html")      #navigating to website
time.sleep(5)
################### input tags
# first_name_locator = '//*[@id="basicBootstrapForm"]/div[1]/div[1]/input'
#
# first_name_web_element = browser.find_element(By.XPATH,first_name_locator)
# first_name_web_element.send_keys("ABCDEF...........")
#
#
# rb_male_name = "radiooptions"
# browser.find_element(By.NAME,rb_male_name).click()
#################################################
# cricket_xpath = "//input[@value='Cricket']"
# crick_obj = browser.find_element(By.XPATH,cricket_xpath)
# crick_obj.click()
#
# cricket_xpath = "//input[@value='Movies']"
# crick_obj = browser.find_element(By.XPATH,cricket_xpath)
# crick_obj.click()
#
# cricket_xpath = "//input[@value='Hockey']"
# crick_obj = browser.find_element(By.XPATH,cricket_xpath)
# crick_obj.click()
#################################################
checkboxes_xpath = "//input[@type='checkbox']"
list_of_obj = browser.find_elements(By.XPATH,checkboxes_xpath)

# list_of_obj[0].click()
# list_of_obj[1].click()

# for web_element in list_of_obj:
#     web_element.click()
#     time.sleep(1.5)

for i in range(0,len(list_of_obj)):     #(0,3)       #0,1,2
    list_of_obj[i].click()      #selecting
    time.sleep(1.5)
    list_of_obj[i].click()      #unslecting
    time.sleep(1)

time.sleep(5)

print("closing the browser")
browser.close()         #closing the browser