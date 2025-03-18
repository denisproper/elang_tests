from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage
from pages.locators import SupportLocators


class SupportPage(BasePage):
    def __init__(self, browser, url):
        super().__init__(browser, url)

    def go_to_support_section(self):
        self.wait.until(EC.element_to_be_clickable(SupportLocators.SUPPORT_SECTION)).click()

    def check_title(self):
        return self.wait.until(EC.presence_of_element_located(SupportLocators.SUPPORT_SECTION))


