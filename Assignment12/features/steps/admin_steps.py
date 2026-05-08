from behave import *
from pages.admin_page import AdminPage
import time

@when('user searches user with below details')
def step_impl(context):

    context.admin = AdminPage(context.driver)

    context.admin.open_admin()

    time.sleep(3)

    for row in context.table:

        key = row[0]
        value = row[1]

        if key == "Username":

            context.admin.enter_username(value)

    context.admin.click_search()

    time.sleep(5)

@then('matching records should be displayed')
def step_impl(context):

    assert "Admin" in context.driver.page_source