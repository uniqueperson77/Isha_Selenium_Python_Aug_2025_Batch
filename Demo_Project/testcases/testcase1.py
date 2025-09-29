from utilities import generic_functions as gf
from pom.redbus import RedBus
import time

def test_case1():
    driver = gf.launch_url("https://www.redbus.in/")
    redbus_obj = RedBus(driver)
    redbus_obj.click_on_account()
    redbus_obj.click_login()
    time.sleep(2.5)
    driver.save_screenshot(r"D:\Isha\SeleniumPythonClass\Demo_Project\results\loginpage.png")
    time.sleep(5)
    driver.quit()