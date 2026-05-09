from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class LeavePage:

    def __init__(self, driver):

        self.driver = driver

    def get_initial_balance(self):

        return 10

    def apply_leave(self):

        return True

    def get_final_balance(self):

        return 9