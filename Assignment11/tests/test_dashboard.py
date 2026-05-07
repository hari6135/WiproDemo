from pages.login_page import LoginPage


def test_dashboard(driver):

    print("\nStarting Dashboard Test")

    login = LoginPage(driver)

    print("Logging into OrangeHRM")

    dashboard = login.login("Admin","admin123")

    print("Dashboard Loaded Successfully")

    assert dashboard.dashboard_heading.is_displayed()

    print("Dashboard Heading Verified")

    print("Dashboard Test Passed")