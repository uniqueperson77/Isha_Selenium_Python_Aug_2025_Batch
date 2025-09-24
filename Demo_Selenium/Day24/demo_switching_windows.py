from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://demo.automationtesting.in/Windows.html")
driver.maximize_window()

click_btn_xpath = '//*[@id="Tabbed"]/a/button'
driver.find_element(By.XPATH,click_btn_xpath).click()   #This opens a new window

print("Opened a new window.")

list_of_windows = driver.window_handles
print(list_of_windows)

driver.switch_to.window(list_of_windows[1])     #shifting driver focus to other window

time.sleep(5)
downloads_xpath = "//a/span[text()='Downloads']"
driver.find_element(By.XPATH,downloads_xpath).click()

time.sleep(5)


# driver.quit()       #close all the windows

driver.close()

time.sleep(2)

driver.switch_to.window(list_of_windows[0])     #shifting driver focus to main window

driver.close()