from behave import *
from pages.pim_page import PimPage

@when('user opens PIM module')
def step_impl(context):

    context.pim = PimPage(context.driver)
    context.pim.open_pim()

@when('user clicks Add Employee')
def step_impl(context):

    context.pim.click_add_employee()

@when('user enters firstname "{fname}"')
def step_impl(context, fname):

    context.pim.enter_firstname(fname)

@when('user enters lastname "{lname}"')
def step_impl(context, lname):

    context.pim.enter_lastname(lname)

@when('user clicks save employee button')
def step_impl(context):

    context.pim.click_save()

@then('employee added successfully')
def step_impl(context):

    assert context.pim.verify_success()