from pages.login_page import LoginPage


def test_employee_details(driver):
    print("\nStarting PIM Test")

    login = LoginPage(driver)

    print("Logging into Application")

    dashboard = login.login("Admin","admin123")

    print("Navigating to PIM Module")

    pim = dashboard.click_pim()

    print("Opening Employee Details")

    details = pim.view_employee_details()

    assert details.is_personal_details_displayed()

    print("Employee Personal Details Page Opened")
    print("PIM Test Passed")