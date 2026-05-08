from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ProfilePage:

    def __init__(self, driver):

        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    myinfo_menu = (
        By.XPATH,
        "//span[text()='My Info']"
    )

    nickname = (
        By.XPATH,
        "(//input[@class='oxd-input oxd-input--active'])[2]"
    )

    upload_btn = (
        By.XPATH,
        "//input[@type='file']"
    )

    save_btn = (
        By.XPATH,
        "//button[@type='submit']"
    )

    def open_myinfo(self):

        self.wait.until(
            EC.element_to_be_clickable(self.myinfo_menu)
        ).click()

    def update_nickname(self, nick):

        import time

        time.sleep(3)

        field = self.wait.until(
            EC.visibility_of_element_located(self.nickname)
        )

        field.clear()
        field.send_keys(nick)

    def upload_image(self, path):

        import time

        time.sleep(5)

        upload = self.wait.until(
            EC.presence_of_element_located(self.upload_btn)
        )

        upload.send_keys(path)

    def click_save(self):

        import time

        time.sleep(3)

        button = self.wait.until(
            EC.element_to_be_clickable(self.save_btn)
        )

        self.driver.execute_script(
            "arguments[0].click();",
            button
        )