import os
import pytest
import allure

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


@pytest.fixture
def driver():

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install())
    )

    driver.maximize_window()

    driver.get("https://www.demoblaze.com/index.html")

    yield driver

    driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):

    outcome = yield

    report = outcome.get_result()

    if report.when == "call" and report.failed:

        driver = item.funcargs["driver"]

        os.makedirs("screenshots", exist_ok=True)

        screenshot_path = (
            f"screenshots/{item.name}.png"
        )

        driver.save_screenshot(screenshot_path)

        allure.attach.file(
            screenshot_path,
            name="Failure Screenshot",
            attachment_type=allure.attachment_type.PNG
        )