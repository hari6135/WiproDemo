from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.category_page import CategoryPage


class HomePage(BasePage):

    LAPTOPS = (By.LINK_TEXT, "Laptops")
    PHONES = (By.LINK_TEXT, "Phones")

    def click_laptops(self):
        self.click(self.LAPTOPS)
        return CategoryPage(self.driver)

    def click_phones(self):
        self.click(self.PHONES)
        return CategoryPage(self.driver)