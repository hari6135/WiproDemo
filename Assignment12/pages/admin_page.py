from selenium.webdriver.common.by import By

class AdminPage:

    def __init__(self, driver):
        self.driver = driver

    admin_menu = (
        By.XPATH,
        "//span[text()='Admin']"
    )

    username = (
        By.XPATH,
        "(//input[@class='oxd-input oxd-input--active'])[2]"
    )

    search_btn = (
        By.XPATH,
        "//button[@type='submit']"
    )

    def open_admin(self):
        self.driver.find_element(*self.admin_menu).click()

    def enter_username(self, uname):
        self.driver.find_element(*self.username).send_keys(uname)

    def click_search(self):
        self.driver.find_element(*self.search_btn).click()