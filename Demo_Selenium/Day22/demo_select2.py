import time
from selenium.webdriver.common.by import By
from selenium import webdriver

driver = webdriver.Chrome()

driver.maximize_window()

website_url = 'https://demo.automationtesting.in/Register.html'
driver.get(website_url)

time.sleep(5)

#click on languages
driver.find_element(By.ID,"msdd").click()

time.sleep(5)

# country_xpath = "//a[text()='Catalan']"
#
# driver.find_element(By.XPATH,country_xpath).click()

countries= ["Bulgarian",'Arabic',"Catalan"]

for country in countries:
    print(country)
    country_xpath = "//a[text()='"+country +"']"
    print(country_xpath)
    driver.find_element(By.XPATH, country_xpath).click()
    time.sleep(0.5)

time.sleep(5)

span_xpath ="//div[text()='Arabic']/span"
driver.find_element(By.XPATH, span_xpath).click()



time.sleep(5)
driver.quit()

# b="INDIA"
# print("Isha"+b+"Isha")