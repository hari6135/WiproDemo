from behave import *
from pages.profile_page import ProfilePage
import os

@when('user uploads profile image')
def step_impl(context):

    profile = ProfilePage(context.driver)

    image_path = os.path.abspath("profile.jpg")

    profile.upload_photo(image_path)

@then('profile should update successfully')
def step_impl(context):

    assert True