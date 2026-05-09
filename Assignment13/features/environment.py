from utils.driver_setup import get_driver
import os

def before_scenario(context, scenario):

    context.driver = get_driver()

    context.driver.maximize_window()

def after_scenario(context, scenario):

    if scenario.status == "failed":

        if not os.path.exists("screenshots"):
            os.makedirs("screenshots")

        screenshot_name = scenario.name.replace(" ","_") + ".png"

        context.driver.save_screenshot(
            f"screenshots/{screenshot_name}"
        )

    context.driver.quit()