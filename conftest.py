from selenium import webdriver
from pytest import fixture
import pytest
import time


@fixture(scope='session')
def driver():
    driver = webdriver.Chrome()
    driver.get('http://the-internet.herokuapp.com/')
    driver.implicitly_wait(15)
    driver.maximize_window()
    yield driver

    # Teardown
    print("   --> Automation practice teardown complete")

