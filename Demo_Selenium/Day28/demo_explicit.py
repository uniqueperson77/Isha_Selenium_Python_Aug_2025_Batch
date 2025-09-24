from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
driver.get("https://demo.automationtesting.in/Register.html")
action_obj = ActionChains(driver)

wait = WebDriverWait(driver=driver,timeout=10)      #Explict wait
fluent_wait = WebDriverWait(driver=driver,timeout=5,poll_frequency=0.25)      #Fluent wait

wait.until(ec.presence_of_element_located((By.XPATH,"//input[@ng-model='FirstName']"))).send_keys("122356")

action_obj.move_to_element(driver.find_element(By.LINK_TEXT,"SwitchTo")).perform()
wait.until(ec.presence_of_element_located((By.LINK_TEXT,"Windows"))).click()


