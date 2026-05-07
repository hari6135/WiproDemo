from selenium.webdriver.common.by import By

from pages.dashboard_page import DashboardPage

class LoginPage:

    def __init__(self, driver):
        self.driver = driver
        self.username = ( By.NAME,"username" )
        self.password = (By.NAME,"password")
        self.login_btn = (By.XPATH,"//button[@type='submit']")

    def login(self, uname, pwd):
        self.driver.find_element(*self.username).send_keys(uname)
        self.driver.find_element(*self.password).send_keys(pwd)
        self.driver.find_element(*self.login_btn).click()

        dashboard = DashboardPage(self.driver)
        dashboard.wait_for_dashboard()

        return dashboard