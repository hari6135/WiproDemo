from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:

    def __init__(self, driver):

        self.driver = driver
        self.wait = WebDriverWait(driver,10)

    username = (By.NAME,"username")
    password = (By.NAME,"password")
    login_btn = (By.XPATH,"//button[@type='submit']")

    def enter_username(self, username):

        self.wait.until(
            EC.visibility_of_element_located(self.username)
        ).send_keys(username)

    def enter_password(self, password):

        self.wait.until(
            EC.visibility_of_element_located(self.password)
        ).send_keys(password)

    def click_login(self):

        self.wait.until(
            EC.element_to_be_clickable(self.login_btn)
        ).click()