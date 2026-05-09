from selenium.webdriver.common.by import By

class AdminPage:

    def __init__(self, driver):

        self.driver = driver

    admin_menu = (By.XPATH, "//span[text()='Admin']")

    username = (
        By.XPATH,
        "(//input[@class='oxd-input oxd-input--active'])[2]"
    )

    search_btn = (By.XPATH, "//button[@type='submit']")

    def search_user(self, data):

        self.driver.find_element(
            *self.admin_menu
        ).click()

        for row in data:

            key = row[0]
            value = row[1]

            if key == "Username":

                self.driver.find_element(
                    *self.username
                ).send_keys(value)

        self.driver.find_element(
            *self.search_btn
        ).click()