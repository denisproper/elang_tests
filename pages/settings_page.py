from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import *

class SettingsPage(BasePage):
    def check_sign_out_button(self):
        return self.is_element_present(*SettingsLocatots.SIGN_OUT_BUTTON)
    
    def check_required_field(self):
        return self.is_element_present(*SettingsLocatots.REQUIRED_FIELD_WARNING)
    
    def click_change_username(self):
        self.click(*SettingsLocatots.CHANGE_USERNAME_BUTTON)

    def click_save_button(self):
        self.click(*SettingsLocatots.SAVE_BUTTON)

    def fill_username_input(self, text):
        self.browser.find_element(*SettingsLocatots.CHANGE_USERNAME_INPUT).send_keys(text)

    def get_current_username(self):
        return self.get_text_from_input(*SettingsLocatots.CURRENT_USERNAME)
 