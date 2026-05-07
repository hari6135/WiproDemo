from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.personal_details_page import PersonalDetailsPage


class PIMPage:

    def __init__(self, driver):
        self.driver = driver

    def view_employee_details(self):

        employee = WebDriverWait(self.driver,10).until(
            EC.element_to_be_clickable((By.XPATH,"(//div[@role='row'])[2]")))

        employee.click()

        return PersonalDetailsPage(
            self.driver
        )