from seleniumpagefactory.Pagefactory import PageFactory

from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC

from pages.pim_page import PIMPage


class DashboardPage(PageFactory):

    def __init__(self, driver):
        self.driver = driver
        self.timeout = 10
    locators ={ "dashboard_heading":("XPATH","//h6[text()='Dashboard']"),
                "pim_menu":("XPATH","//span[text()='PIM']")}

    def wait_for_dashboard(self):
        WebDriverWait(self.driver,10).until(
            EC.visibility_of_element_located((By.XPATH,"//h6[text()='Dashboard']")))

        return self

    def click_pim(self):
        self.pim_menu.click()
        return PIMPage(self.driver)