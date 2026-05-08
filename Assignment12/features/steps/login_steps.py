from behave import *
from utils.driver_setup import get_driver
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from utils.config import URL
import time

@given('user navigates to OrangeHRM login page')
def step_impl(context):

    context.driver = get_driver()
    context.driver.get(URL)

    time.sleep(3)

    context.login = LoginPage(context.driver)

@when('user enters username "{username}"')
def step_impl(context, username):

    context.login.enter_username(username)

@when('user enters password "{password}"')
def step_impl(context, password):

    context.login.enter_password(password)

@when('user clicks login button')
def step_impl(context):

    context.login.click_login()

@then('dashboard page should be displayed')
def step_impl(context):

    dashboard = DashboardPage(context.driver)

    assert dashboard.verify_dashboard()

@then('invalid credential message should be displayed')
def step_impl(context):

    assert "Invalid credentials" in context.driver.page_source