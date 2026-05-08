from behave import *
from utils.driver_setup import get_driver
from utils.config import *
from pages.login_page import LoginPage
import time

@given('user logs into OrangeHRM application')
def step_impl(context):

    context.driver = get_driver()

    context.driver.get(URL)

    login = LoginPage(context.driver)

    login.enter_username(USERNAME)
    login.enter_password(PASSWORD)
    login.click_login()

    time.sleep(3)