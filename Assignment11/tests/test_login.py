from pages.login_page import LoginPage


def test_valid_login(driver):

    print("\nStarting Login Test")

    login = LoginPage(driver)

    print("Entering Username and Password")

    login.login("Admin","admin123")

    print("Login Successful")

    print("Login Test Passed")