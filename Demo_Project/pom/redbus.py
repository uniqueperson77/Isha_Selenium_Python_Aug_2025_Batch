import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

class RedBus:
    account_icon_xpath = "//div[text()='Account']"
    login_btn_xpath = "//button[text()='Log in']"
    from_xpath = "//div[text()='From']"
    to_xpath = "//div[text()='To']"
    src_id = "srcDest"
    search_buses_button_xpath = "//button[text()='Search buses']"
    search_suggestions_xpath = "//div[@aria-label='Search suggestions list']//div[@role='heading']"
    tomorrow_xpath = "//button[text()='Tomorrow']"
    num_of_buses_xpath = "//span[contains(@class,'subtitle')]"

    def __init__(self,driver):
        self.driver = driver

    def click_on_account(self):
        self.driver.find_element(By.XPATH,self.account_icon_xpath).click()

    def click_login(self):
        self.driver.find_element(By.XPATH,self.login_btn_xpath).click()

    def click_on_search_buses(self):
        self.driver.find_element(By.XPATH, self.search_buses_button_xpath).click()

    def select_search_suggestion(self):
        time.sleep(2.5)
        list_of_places_elements = self.driver.find_elements(By.XPATH, self.search_suggestions_xpath)
        list_of_places_elements[0].click()

    def enter_source(self,place_name):
        self.driver.find_element(By.XPATH, self.from_xpath).click()
        self.driver.find_element(By.ID, self.src_id).send_keys(place_name)

    def enter_destination(self,place_name):
        # self.driver.find_element(By.XPATH, self.to_xpath).click()
        self.driver.find_element(By.ID, self.src_id).send_keys(place_name)

    def click_on_tomorrow(self):
        self.driver.find_element(By.XPATH,self.tomorrow_xpath).click()
        time.sleep(5)

    def get_number_of_buses(self):
        full_text = self.driver.find_element(By.XPATH, self.num_of_buses_xpath).text
        num_of_buses = (full_text.split(" buses"))[0]
        print("Number of buses = "+ str(num_of_buses))
        return num_of_buses
