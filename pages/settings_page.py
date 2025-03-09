import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from .base_page import BasePage
from .locators import *

class SettingsPage(BasePage):
    def check_sign_out_button(self):
        return self.wait.until(EC.presence_of_element_located(SettingsLocators.SIGN_OUT_BUTTON))

    def check_required_field(self):
        return self.wait.until(EC.presence_of_element_located(SettingsLocators.REQUIRED_FIELD_WARNING))

    def check_is_privacy_policy_present(self):
        return self.wait.until(EC.presence_of_element_located(SettingsLocators.PRIVACY_POLICY_TEXT))

    def click_change_username(self):
        self.wait.until(EC.element_to_be_clickable(SettingsLocators.CHANGE_USERNAME_BUTTON)).click()

    def click_pointer_to_the_top(self):
        self.wait.until(EC.element_to_be_clickable(SettingsLocators.POINTER_TO_THE_TOP)).click()

    def click_save_button(self):
        self.wait.until(EC.element_to_be_clickable(SettingsLocators.SAVE_BUTTON)).click()

    def select_language(self, locator, text="English"):
        select_element = self.wait.until(EC.element_to_be_clickable(locator))
        self.scroll_to_element(select_element)
        select = Select(select_element)
        select.select_by_visible_text(text)

    def select_language_of_i_learn_button(self, text="English"):
        self.select_language(SettingsLocators.I_LEARN_SELECT_BUTTON, text)

    def select_language_of_translate_into_button(self, text="English"):
        self.select_language(SettingsLocators.TRANSLATE_INTO_SELECT_BUTTON, text)

    def select_language_of_interface_button(self, text="English"):
        self.select_language(SettingsLocators.INTERFACE_LANGUAGE_BUTTON, text)

    def fill_username_input(self, text):
        input_element = self.wait.until(EC.element_to_be_clickable(SettingsLocators.CHANGE_USERNAME_INPUT))
        input_element.clear()
        input_element.send_keys(text)

    def get_current_username(self):
        return self.wait.until(EC.visibility_of_element_located(SettingsLocators.CURRENT_USERNAME)).text

    def click_privacy_policy_button(self):
        self.wait.until(EC.element_to_be_clickable(SettingsLocators.PRIVACY_POLICY_BUTTON)).click()

    def check_is_privacy_policy_text_displayed(self):
        return self.wait.until(EC.visibility_of_element_located(SettingsLocators.PRIVACY_POLICY_TEXT)).is_displayed()

    def get_selected_option(self, locator):
        select_element = self.wait.until(EC.presence_of_element_located(locator))
        select = Select(select_element)
        return select.first_selected_option.text

    def get_selected_option_for_i_learn_button(self):
        return self.get_selected_option(SettingsLocators.I_LEARN_SELECT_BUTTON)

    def get_selected_option_for_translate_into_button(self):
        return self.get_selected_option(SettingsLocators.TRANSLATE_INTO_SELECT_BUTTON)

    def get_selected_option_for_interface_language_button(self):
        return self.get_selected_option(SettingsLocators.INTERFACE_LANGUAGE_BUTTON)

    def get_text_of_sign_out_button(self):
        element = self.wait.until(EC.visibility_of_element_located(SettingsLocators.SIGN_OUT_BUTTON))
        self.scroll_to_element(element)
        return element.text
