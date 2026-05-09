from behave import *
from pages.admin_page import AdminPage

@when('I enter the following search criteria:')
def step_impl(context):

    admin = AdminPage(context.driver)

    admin.search_user(context.table)

@then('matching admin records should appear')
def step_impl(context):

    assert "Admin" in context.driver.page_source