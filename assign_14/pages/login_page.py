from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage


class LoginPage(BasePage):

    LOGIN_HEADER = (By.ID, "login2")

    USERNAME = (By.ID, "loginusername")

    PASSWORD = (By.ID, "loginpassword")

    MODAL_LOGIN_BUTTON = (
        By.XPATH,
        "//div[@id='logInModal']//button[text()='Log in']"
    )

    def open_login_modal(self):

        self.click(self.LOGIN_HEADER)

        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(
                self.USERNAME
            )
        )

    def login(self, username, password):

        self.find(self.USERNAME).send_keys(username)

        self.find(self.PASSWORD).send_keys(password)

        self.click(self.MODAL_LOGIN_BUTTON)

        alert = WebDriverWait(self.driver, 10).until(
            EC.alert_is_present()
        )

        alert_text = alert.text

        alert.accept()

        return alert_text