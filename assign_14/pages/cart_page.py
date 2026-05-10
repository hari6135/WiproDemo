from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from pages.purchase_modal import PurchaseModal


class CartPage(BasePage):

    PLACE_ORDER = (By.XPATH, "//button[text()='Place Order']")
    SUCCESS_MESSAGE = (By.CLASS_NAME, "sweet-alert")

    def click_place_order(self):

        self.click(self.PLACE_ORDER)

        return PurchaseModal(self.driver)

    def verify_success_message(self):

        return "Thank you for your purchase!" in self.driver.page_source