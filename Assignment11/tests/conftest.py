import pytest
import time
from selenium import webdriver


@pytest.fixture
def driver():

    driver = webdriver.Edge()
    driver.maximize_window()
    driver.get("https://opensource-demo.orangehrmlive.com/")
    time.sleep(3)

    yield driver
    driver.quit()