from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()
driver.get("https://demo.automationtesting.in/Datepicker.html")
time.sleep(5)

driver.find_element(By.ID,"datepicker1").click()
#now calendar appears
time.sleep(3)

month = 1
date = 25

def select_date():
    next_locator = "//a[@title='Next']"
    prev_locator = "//a[@title='Prev']"

    # driver.find_element(By.XPATH,next_locator).click()
    for i in range(8):
        driver.find_element(By.XPATH, prev_locator).click()
        time.sleep(0.25)
    time.sleep(3)
    driver.find_element(By.LINK_TEXT,"1").click()
    time.sleep(4)


def select_todays_date(driver):
    xpath = "//a[text()='22']"
    driver.find_element(By.LINK_TEXT,"22").click()
    time.sleep(5)

def select_month_date(month,date):
    next_locator = "//a[@title='Next']"
    prev_locator = "//a[@title='Prev']"
    current_month = 9

    if month>current_month:
        locator = next_locator
        no_of_clicks = month-current_month
    else:
        locator = prev_locator
        no_of_clicks = current_month-month


    for i in range(no_of_clicks):
        driver.find_element(By.XPATH, locator).click()
        # time.sleep(0.25)
    time.sleep(3)
    driver.find_element(By.LINK_TEXT,str(date)).click()
    time.sleep(4)


select_month_date(month, date)