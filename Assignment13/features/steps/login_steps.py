from behave import *
from pages.login_page import LoginPage
from utils.config import URL

@given('user navigates to OrangeHRM login page')
def step_impl(context):

    context.driver.get(URL)

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

    assert "dashboard" in context.driver.current_url.lower()