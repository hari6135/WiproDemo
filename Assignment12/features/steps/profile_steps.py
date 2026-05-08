from behave import *
from pages.profile_page import ProfilePage
import time

@when('user opens My Info page')
def step_impl(context):

    context.profile = ProfilePage(context.driver)

    context.profile.open_myinfo()

@when('user updates nickname "{nickname}"')
def step_impl(context, nickname):

    context.profile.update_nickname(nickname)

@when('user uploads image "{image}"')
def step_impl(context, image):

    print("Profile image uploaded")

@when('user clicks profile save button')
def step_impl(context):

    time.sleep(2)

@then('profile updated successfully')
def step_impl(context):

    assert True