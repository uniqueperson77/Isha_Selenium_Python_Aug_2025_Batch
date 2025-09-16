from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()

driver.maximize_window()

website_url = 'https://demo.automationtesting.in/Register.html'
driver.get(website_url)

time.sleep(5)

select_web_element = driver.find_element(By.ID,"Skills")

list_of_dd_web_elements = driver.find_elements(By.XPATH,"//select[@id='Skills']/option")

# for web_ele in list_of_dd_web_elements:
#     print(web_ele.text)


# for index in range(len(list_of_dd_web_elements)):
#     print(list_of_dd_web_elements[index].text)
#     if list_of_dd_web_elements[index].text == "Backup Management":
#         select_obj = Select(select_web_element)
#         select_obj.select_by_index(index)
#         break


select_obj = Select(select_web_element)


# select_obj.select_by_index(4)
# select_obj.select_by_value("iOS")
select_obj.select_by_visible_text("iOS")
time.sleep(5)

driver.quit()







