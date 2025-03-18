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

    def input_name_field(self, text):
        search_field = self.wait.until(EC.presence_of_element_located(SupportLocators.NAME_INPUT))
        search_field.clear()
        search_field.send_keys(text)

    def input_email_field(self, text):
        search_field = self.wait.until(EC.presence_of_element_located(SupportLocators.EMAIL_INPUT))
        search_field.clear()
        search_field.send_keys(text)

    def input_message_field(self, text):
        search_field = self.wait.until(EC.presence_of_element_located(SupportLocators.MESSAGE_INPUT))
        search_field.clear()
        search_field.send_keys(text)

    def check_success_message_is_displayed(self):
        return self.wait.until(EC.visibility_of_element_located(SupportLocators.SUCCESSFUL_MESSAGE))

    def click_submit_button(self):
        button = self.wait.until(EC.element_to_be_clickable(SupportLocators.SEND_MESSAGE_BUTTON))
        self.scroll_and_click(button)


