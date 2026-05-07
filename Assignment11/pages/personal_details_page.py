class PersonalDetailsPage:

    def __init__(self, driver):

        self.driver = driver

    def is_personal_details_displayed(self):

        return "viewPersonalDetails" in self.driver.current_url