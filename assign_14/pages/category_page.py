from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage
from pages.product_details_page import ProductDetailsPage


class CategoryPage(BasePage):

    PRODUCTS = (By.CLASS_NAME, "hrefch")

    def verify_laptop_list_presence(self):

        WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located(
                self.PRODUCTS
            )
        )

        return len(
            self.driver.find_elements(*self.PRODUCTS)
        ) > 0

    def get_all_product_names(self):

        WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located(
                self.PRODUCTS
            )
        )

        while True:

            try:

                products = self.driver.find_elements(
                    *self.PRODUCTS
                )

                names = []

                for product in products:
                    names.append(product.text)

                return names

            except Exception:

                continue
    def select_product(self, product_name):

        WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located(
                self.PRODUCTS
            )
        )

        while True:

            try:

                products = self.driver.find_elements(
                    *self.PRODUCTS
                )

                for product in products:

                    product_text = product.text

                    if product_text == product_name:
                        product.click()

                        return ProductDetailsPage(
                            self.driver
                        )

            except Exception:

                continue