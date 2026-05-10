from pages.login_page import LoginPage


def test_invalid_login(driver):

    login = LoginPage(driver)

    login.open_login_modal()

    alert_text = login.login(
        "testuser",
        "wrongpassword"
    )

    assert alert_text == "Success"