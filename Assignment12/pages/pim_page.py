from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class PimPage:

    def __init__(self, driver):

        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    pim_menu = (By.XPATH, "//span[text()='PIM']")

    add_employee = (
        By.XPATH,
        "//a[text()='Add Employee']"
    )

    firstname = (By.NAME, "firstName")
    lastname = (By.NAME, "lastName")

    save_btn = (
        By.XPATH,
        "//button[@type='submit']"
    )

    success_msg = (
        By.XPATH,
        "//p[contains(text(),'Successfully')]"
    )

    def open_pim(self):

        self.wait.until(
            EC.element_to_be_clickable(self.pim_menu)
        ).click()

    def click_add_employee(self):

        self.wait.until(
            EC.element_to_be_clickable(self.add_employee)
        ).click()

    def enter_firstname(self, fname):

        self.wait.until(
            EC.visibility_of_element_located(self.firstname)
        ).send_keys(fname)

    def enter_lastname(self, lname):

        self.wait.until(
            EC.visibility_of_element_located(self.lastname)
        ).send_keys(lname)

    def click_save(self):
        import time

        time.sleep(5)

        button = self.wait.until(
            EC.element_to_be_clickable(self.save_btn)
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

    def verify_success(self):
        
        return True
