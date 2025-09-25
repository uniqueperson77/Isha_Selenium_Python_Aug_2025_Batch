import time

from selenium import webdriver
from selenium.webdriver.common.by import By

class RedBus:
    account_icon_xpath = "//span[text()='Account']"
    from_xpath = "//div[text()='From']"
    to_xpath = "//div[text()='To']"
    src_id = "srcDest"
    search_buses_button_xpath = "//button[text()='Search buses']"
    search_suggestions_xpath = "//div[@aria-label='Search suggestions list']//div[@role='heading']"
    def __init__(self,driver):
        self.driver = driver

    def click_on_account(self):
        self.driver.find_element(By.XPATH,self.account_icon_xpath).click()

    def click_on_search_buses(self):
        self.driver.find_element(By.XPATH, self.search_buses_button_xpath).click()

    def select_search_suggestion(self):
        list_of_places_elements = self.driver.find_elements(By.XPATH, self.search_suggestions_xpath)
        list_of_places_elements[0].click()

    def enter_source(self,place_name):
        self.driver.find_element(By.XPATH, self.from_xpath).click()
        self.driver.find_element(By.ID, self.src_id).send_keys(place_name)
        time.sleep(2)

    def enter_destination(self,place_name):
        # self.driver.find_element(By.XPATH, self.to_xpath).click()
        self.driver.find_element(By.ID, self.src_id).send_keys(place_name)
        time.sleep(2)