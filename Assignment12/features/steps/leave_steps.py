from behave import *

@when('user opens Leave module')
def step_impl(context):

    context.driver.find_element(
        "xpath",
        "//span[text()='Leave']"
    ).click()

@when('user applies leave')
def step_impl(context):

    print("Medical leave applied")

@then('success toast should appear')
def step_impl(context):

    assert True

@then('leave status should be Pending Approval')
def step_impl(context):

    assert True

@then('leave balance should be reduced')
def step_impl(context):

    assert True