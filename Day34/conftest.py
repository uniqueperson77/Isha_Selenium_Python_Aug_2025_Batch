import pytest,time
import pytest_html
from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from pytest_metadata.plugin import metadata_key



def pytest_configure(config):
    config.stash[metadata_key]["Environemnt"] = "TEST4"

def pytest_html_report_title(report):
    report.title = "Test Automation"

@pytest.fixture(scope='function')
def setup_and_teardown_emirates():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)
    wait = WebDriverWait(driver,10)
    driver.get("https://www.emirates.com/in/english/")
    try:
        wait.until(ec.presence_of_element_located((By.XPATH,"//button[text()='Accept']"))).click()
    except:
        pass
    yield driver
    time.sleep(0.25)
    driver.quit()

@pytest.fixture(scope='function')
def click_emirates_home():
    pass


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    extras = getattr(report, "extras", [])
    if report.when == "call":
        # always add url to report
        extras.append(pytest_html.extras.url("https://www.emirates.com/in/english/"))
        xfail = hasattr(report, "wasxfail")

        if (report.skipped and xfail) or (report.failed and not xfail):
            extras.append(pytest_html.extras.png(r"D:\Isha\SeleniumPythonClass\test1.png"))
            # # only add additional html on failure
            # extras.append(pytest_html.extras.html("<div>Additional HTML</div>"))
            # # only add additional html on failure
            # extras.append(pytest_html.extras.html("<div>Additional HTML</div>"))
        report.extras = extras
