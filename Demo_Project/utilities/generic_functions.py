from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

def launch_url(url,choose_browser='Chrome'):
    if choose_browser=='Chrome':
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    elif choose_browser == 'FireFox':
        driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
    elif choose_browser == 'Edge':
        driver = webdriver.Edge()

    driver.maximize_window()
    driver.get(url)
    driver.implicitly_wait(5)
    return driver