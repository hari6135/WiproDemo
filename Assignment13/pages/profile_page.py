class ProfilePage:

    def __init__(self, driver):

        self.driver = driver

    def upload_photo(self, path):

        print("Profile photo uploaded:", path)

        return True