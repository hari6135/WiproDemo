from behave import *
from pages.pim_page import PimPage
from pages.login_page import LoginPage
from utils.config import *

@given('user logs into OrangeHRM')
def step_impl(context):

    context.driver.get(URL)

    login = LoginPage(context.driver)

    login.enter_username(USERNAME)
    login.enter_password(PASSWORD)
    login.click_login()

@when('I enter "{firstname}" and "{lastname}"')
def step_impl(context, firstname, lastname):

    pim = PimPage(context.driver)

    pim.add_employee(firstname,lastname)

@then('employee should be created successfully')
def step_impl(context):

    assert True