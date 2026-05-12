from selenium.webdriver.common.by import By
from robot.libraries.BuiltIn import BuiltIn


class ProductPage:

    def get_product_price_by_name(self, product_name):

        selenium_lib = BuiltIn().get_library_instance(
            'SeleniumLibrary'
        )

        driver = selenium_lib.driver

        products = driver.find_elements(
            By.CLASS_NAME,
            "inventory_item"
        )

        for product in products:

            name = product.find_element(
                By.CLASS_NAME,
                "inventory_item_name"
            ).text

            if name == product_name:

                price = product.find_element(
                    By.CLASS_NAME,
                    "inventory_item_price"
                ).text

                price = price.replace("$", "")

                return float(price)

        return 0.0