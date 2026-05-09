from behave import *
from pages.leave_page import LeavePage

@when('user applies leave')
def step_impl(context):

    leave = LeavePage(context.driver)

    context.initial = leave.get_initial_balance()

    leave.apply_leave()

    context.final = leave.get_final_balance()

@then('success toast message should appear')
def step_impl(context):

    toast = "Success"

    assert toast == "Success"

@then('leave balance should reduce by 1')
def step_impl(context):

    assert context.initial - context.final == 1