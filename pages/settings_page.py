import time
from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import *



class SettingsPage(BasePage):
    def check_sign_out_button(self):
        return self.is_element_present(*SettingsLocatots.SIGN_OUT_BUTTON)
    
    def check_required_field(self):
        return self.is_element_present(*SettingsLocatots.REQUIRED_FIELD_WARNING)
    
    def check_is_privacy_policy_present(self):
        return self.is_element_present(*SettingsLocatots.PRIVACY_POLICY_TEXT)
    
    def click_change_username(self):
        self.click(*SettingsLocatots.CHANGE_USERNAME_BUTTON)

    def click_pointer_to_the_top(self):
        self.click(*SettingsLocatots.POINTER_TO_THE_TOP)

    def click_save_button(self):
        self.click(*SettingsLocatots.SAVE_BUTTON)

    def select_language_of_i_learn_button(self, text: str = "English"):
        select_element = self.browser.find_element(*SettingsLocatots.I_LEARN_SELECT_BUTTON)
        self.scroll_to_element(*SettingsLocatots.I_LEARN_SELECT_BUTTON)
        select = Select(select_element)
        time.sleep(1)
        select.select_by_visible_text(text)
        time.sleep(1)

    def select_language_of_translate_into_button(self, text: str = "English"):
        select_element = self.browser.find_element(*SettingsLocatots.TRANSLATE_INTO_SELECT_BUTTON)
        self.scroll_to_element(*SettingsLocatots.TRANSLATE_INTO_SELECT_BUTTON)
        select = Select(select_element)
        time.sleep(1)
        select.select_by_visible_text(text)
        time.sleep(1)

    def select_language_of_interface_button(self, text: str = "English"):
        select_element = self.browser.find_element(*SettingsLocatots.INTERFACE_LANGUAGE_BUTTON)
        self.scroll_to_element(*SettingsLocatots.INTERFACE_LANGUAGE_BUTTON)
        select = Select(select_element)
        time.sleep(1)
        select.select_by_visible_text(text)
        time.sleep(1)
        

    def fill_username_input(self, text):
        self.browser.find_element(*SettingsLocatots.CHANGE_USERNAME_INPUT).send_keys(text)

    def get_current_username(self):
        return self.get_text_from_input(*SettingsLocatots.CURRENT_USERNAME)
    
    def click_privacy_policy_button(self):
        self.click(*SettingsLocatots.PRIVACY_POLICY_BUTTON)

    def check_is_privacy_policy_text_displayed(self):
        return self.browser.find_element(*SettingsLocatots.PRIVACY_POLICY_TEXT).is_displayed()
       
    def get_selected_option_for_i_learn_button(self):
        select_element = self.browser.find_element(*SettingsLocatots.I_LEARN_SELECT_BUTTON)
        select = Select(select_element)
        return select.first_selected_option.text
    
    def get_selected_option_for_translate_into_button(self):
        select_element = self.browser.find_element(*SettingsLocatots.TRANSLATE_INTO_SELECT_BUTTON)
        select = Select(select_element)
        return select.first_selected_option.text
    

    def get_selected_option_for_interface_language_button(self):
        select_element = self.browser.find_element(*SettingsLocatots.INTERFACE_LANGUAGE_BUTTON)
        select = Select(select_element)
        return select.first_selected_option.text
    
    def get_text_of_sign_out_button(self):
        self.scroll_to_element(*SettingsLocatots.SIGN_OUT_BUTTON)
        time.sleep(1)
        return self.get_text_from_input(*SettingsLocatots.SIGN_OUT_BUTTON)