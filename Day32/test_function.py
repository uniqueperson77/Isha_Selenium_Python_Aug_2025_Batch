import pytest

@pytest.fixture()
def navigate_to_url():
    print("Browser is launched")

@pytest.mark.usefixtures("navigate_to_url")
def test_login1():
    print("Application logged on")

def test_login2(navigate_to_url):
    print("Application logged on")

def test_logout():
    print("Logged out from session")

