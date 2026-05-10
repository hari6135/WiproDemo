from pages.home_page import HomePage


def test_phone_products(driver):

    home = HomePage(driver)

    category = home.click_phones()

    products = category.get_all_product_names()

    assert "Samsung galaxy s6" in products