import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.home_page import HomePage
from pages.cart_page import CartPage


def test_checkout(driver):

    home = HomePage(driver)

    laptops = home.click_laptops()

    product = laptops.select_product("Sony vaio i5")

    product.add_product_to_cart()

    driver.find_element(By.ID, "cartur").click()

    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(
            (By.XPATH, "//button[text()='Place Order']")
        )
    )

    cart = CartPage(driver)

    modal = cart.click_place_order()

    data = {
        "name": "Alex",
        "country": "India",
        "city": "Chennai",
        "card": "123456789",
        "month": "May",
        "year": "2026"
    }

    modal.fill_purchase_form(data)

    modal.click_purchase()

    assert cart.verify_success_message()