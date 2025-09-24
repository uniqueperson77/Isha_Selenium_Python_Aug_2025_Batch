import time
from selenium.webdriver.common.by import By
from selenium import webdriver


class Demo_Alerts:
    def demo_alerts1(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://demo.automationtesting.in/Alerts.html")
        time.sleep(5)
        ok_btn_xpath = "//button[@class='btn btn-danger']"
        # web_ele = driver.find_element(By.XPATH,ok_btn_xpath)
        # web_ele.click()
        driver.find_element(By.XPATH, ok_btn_xpath).click()     #this st clicking btn
        print("Alert has been displayed")
        time.sleep(3)
        driver.switch_to.alert.accept()
        print("Alert has been accepted")
        time.sleep(3)

    def demo_alerts3(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://demo.automationtesting.in/Alerts.html")
        time.sleep(5)
        #clicking on Alert with Textbox
        driver.find_element(By.XPATH,"/html/body/div[1]/div/div/div/div[1]/ul/li[3]/a").click()
        driver.find_element(By.XPATH,"//button[@class='btn btn-info']").click()
        time.sleep(2)
        driver.switch_to.alert.send_keys("Hellooooo World!!!!!!!!!!")
        driver.switch_to.alert.accept()
        time.sleep(5)



obj = Demo_Alerts()
obj.demo_alerts3()


