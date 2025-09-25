from selenium import webdriver

def launch_url(url):
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(url)
    driver.implicitly_wait(5)
    return driver