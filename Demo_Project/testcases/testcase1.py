from utilities import generic_functions as gf
from pom.redbus import RedBus
import time

driver = gf.launch_url("https://www.redbus.in/")

redbus_obj = RedBus(driver)

#pick one source
redbus_obj.enter_source("Hyderabad")
redbus_obj.select_search_suggestion()

time.sleep(5)
#pick one destination
redbus_obj.enter_destination("Mumbai")
redbus_obj.select_search_suggestion()

redbus_obj.click_on_search_buses()

time.sleep(15)