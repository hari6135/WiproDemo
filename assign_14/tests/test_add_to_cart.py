import time

from pages.home_page import HomePage


def test_add_product_to_cart(driver):

    home = HomePage(driver)

    laptops = home.click_laptops()

    product = laptops.select_product("Sony vaio i5")

    product.add_product_to_cart()

    time.sleep(2)