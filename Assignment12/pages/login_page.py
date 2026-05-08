from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    username = (By.NAME, "username")
    password = (By.NAME, "password")
    login_btn = (By.XPATH, "//button[@type='submit']")

    error_msg = (
        By.XPATH,
        "//p[contains(text(),'Invalid credentials')]"
    )

    def enter_username(self, uname):

        self.wait.until(
            EC.visibility_of_element_located(self.username)
        ).send_keys(uname)

    def enter_password(self, pwd):

        self.wait.until(
            EC.visibility_of_element_located(self.password)
        ).send_keys(pwd)

    def click_login(self):

        self.wait.until(
            EC.element_to_be_clickable(self.login_btn)
        ).click()

    def get_error_message(self):

        return self.wait.until(
            EC.visibility_of_element_located(self.error_msg)
        ).text