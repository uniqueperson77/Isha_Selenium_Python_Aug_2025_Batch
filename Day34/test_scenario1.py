import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


def test_testcase1(setup_and_teardown_emirates):
    driver = setup_and_teardown_emirates
    driver.find_element(By.PARTIAL_LINK_TEXT,"LOG IN").click()

def test_testcase2(setup_and_teardown_emirates):
    driver = setup_and_teardown_emirates
    driver.find_element(By.XPATH,"//button[@data-link='BOOK']").click()

def test_testcase3(setup_and_teardown_emirates):
    driver = setup_and_teardown_emirates
    driver.find_element(By.XPATH,"//button[@data-link='MANAGE']").click()

def test_testcase4(setup_and_teardown_emirates):
    driver = setup_and_teardown_emirates
    driver.find_element(By.XPATH,"//button[@data-link='HELP']").click()

def test_testcase5(setup_and_teardown_emirates):
    driver = setup_and_teardown_emirates
    driver.find_element(By.XPATH,"//button[@data-link='BOOK']").click()

def test_testcase6(setup_and_teardown_emirates):
    driver = setup_and_teardown_emirates
    driver.find_element(By.XPATH,"//button[@data-link='MANAGE']").click()

def test_testcase7(setup_and_teardown_emirates):
    driver = setup_and_teardown_emirates
    driver.find_element(By.XPATH,"//button[@data-link='HELP']").click()

def test_testcase8(setup_and_teardown_emirates):
    driver = setup_and_teardown_emirates
    driver.find_element(By.PARTIAL_LINK_TEXT,"LOG IN").click()





