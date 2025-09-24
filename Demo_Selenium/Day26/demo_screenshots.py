import time

from selenium import webdriver
from selenium.webdriver.common.by import By

from Screenshot import Screenshot

browser = webdriver.Chrome()
browser.maximize_window()
browser.get("https://demo.automationtesting.in/Register.html")
time.sleep(5)

#visible portion
browser.save_screenshot(r"D:\Isha\SeleniumPythonClass\Demo_Selenium\Day26\Screenshots\image1.png")

web_element = browser.find_element(By.XPATH,"//input[@placeholder='Last Name']")
web_element.screenshot(r"D:\Isha\SeleniumPythonClass\Demo_Selenium\Day26\Screenshots\image2.png")

obj = Screenshot(browser)
obj.capture_full_page(r"D:\Isha\SeleniumPythonClass\Demo_Selenium\Day26\Screenshots\image3.png")

browser.quit()