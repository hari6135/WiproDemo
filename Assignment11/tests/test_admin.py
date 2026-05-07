import pytest

from pages.login_page import LoginPage
from pages.admin_page import AdminPage
from utils.data_provider import test_users


@pytest.mark.parametrize("username",test_users)
def test_user_exists(driver, username):

    print(f"\nStarting Admin Test for User: {username}")

    login = LoginPage(driver)

    print("Logging into Application")

    login.login("Admin","admin123")

    admin = AdminPage(driver)

    print("Navigating to Admin Module")

    admin.side_menu.click_admin()

    print("Checking User in Admin Table")

    result = admin.verify_user_exists(username)

    print(f"User Verification Result: {username} -> {result}")

    print("Admin Test Completed")