from selenium.webdriver.common.by import By

from pages.components.side_menu_component import SideMenuComponent

class AdminPage:

    def __init__(self, driver):
        self.driver = driver
        self.side_menu = SideMenuComponent(driver)

    def get_all_users(self):
        users = self.driver.find_elements(By.XPATH,"//div[@role='row']/div[2]")

        usernames = []
        for user in users:

            usernames.append(user.text)

        return usernames

    def verify_user_exists(self, username):
        return username in self.get_all_users()