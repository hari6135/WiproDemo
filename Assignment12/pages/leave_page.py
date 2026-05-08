from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LeavePage:

    def __init__(self, driver):

        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    leave_menu = (
        By.XPATH,
        "//span[text()='Leave']"
    )

    apply_btn = (
        By.XPATH,
        "//a[text()='Apply']"
    )

    submit_btn = (
        By.XPATH,
        "//button[@type='submit']"
    )

    def open_leave(self):

        self.wait.until(
            EC.element_to_be_clickable(self.leave_menu)
        ).click()

    def apply_leave(self):

        self.wait.until(
            EC.element_to_be_clickable(self.apply_btn)
        ).click()

    def submit_leave(self):
        import time

        time.sleep(5)

        button = self.wait.until(
            EC.element_to_be_clickable(self.submit_btn)
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView();",
            button
        )

        time.sleep(2)

        self.driver.execute_script(
            "arguments[0].click();",
            button
        )