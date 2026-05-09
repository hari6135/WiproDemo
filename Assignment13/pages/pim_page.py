from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class PimPage:

    def __init__(self, driver):

        self.driver = driver
        self.wait = WebDriverWait(driver,10)

    pim_menu = (By.XPATH,"//span[text()='PIM']")
    add_btn = (By.XPATH,"//a[text()='Add Employee']")
    firstname = (By.NAME,"firstName")
    lastname = (By.NAME,"lastName")
    save_btn = (By.XPATH,"//button[@type='submit']")

    def add_employee(self, fname, lname):

        self.wait.until(
            EC.element_to_be_clickable(self.pim_menu)
        ).click()

        self.wait.until(
            EC.element_to_be_clickable(self.add_btn)
        ).click()

        self.wait.until(
            EC.visibility_of_element_located(self.firstname)
        ).send_keys(fname)

        self.driver.find_element(*self.lastname).send_keys(lname)

        save = self.wait.until(
            EC.element_to_be_clickable(self.save_btn)
        )

        save.click()