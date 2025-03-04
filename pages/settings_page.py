import time

import allure

from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import *



class SettingsPage(BasePage):
    with allure.step("Проверка отображения кнопки выхода из аккаунта"):
        def check_sign_out_button(self):
            return self.is_element_present(*SettingsLocators.SIGN_OUT_BUTTON)


    with allure.step("Проверка отображения кнопки о вводе непустого имени"):
        def check_required_field(self):
            return self.is_element_present(*SettingsLocators.REQUIRED_FIELD_WARNING)


    with allure.step("Проверка отображения кнопки приватной политики"):
        def check_is_privacy_policy_present(self):
            return self.is_element_present(*SettingsLocators.PRIVACY_POLICY_TEXT)


    with allure.step("Клик на кнопку смены юзернейма"):
        def click_change_username(self):
            self.click(*SettingsLocators.CHANGE_USERNAME_BUTTON)


    with allure.step("Клик на кнопку скролла вверх"):
        def click_pointer_to_the_top(self):
            self.click(*SettingsLocators.POINTER_TO_THE_TOP)


    with allure.step("Клик на кнопку сохранения "):
        def click_save_button(self):
            self.click(*SettingsLocators.SAVE_BUTTON)


    with allure.step("Выбор языка для изучения"):
        def select_language_of_i_learn_button(self, text: str = "English"):
            select_element = self.browser.find_element(*SettingsLocators.I_LEARN_SELECT_BUTTON)
            self.scroll_to_element(*SettingsLocators.I_LEARN_SELECT_BUTTON)
            select = Select(select_element)
            time.sleep(1)
            select.select_by_visible_text(text)
            time.sleep(1)


    with allure.step("Выбор родного языка"):
        def select_language_of_translate_into_button(self, text: str = "English"):
            select_element = self.browser.find_element(*SettingsLocators.TRANSLATE_INTO_SELECT_BUTTON)
            self.scroll_to_element(*SettingsLocators.TRANSLATE_INTO_SELECT_BUTTON)
            select = Select(select_element)
            time.sleep(1)
            select.select_by_visible_text(text)
            time.sleep(1)


    with allure.step("Выбор языка интерфейса"):
        def select_language_of_interface_button(self, text: str = "English"):
            select_element = self.browser.find_element(*SettingsLocators.INTERFACE_LANGUAGE_BUTTON)
            self.scroll_to_element(*SettingsLocators.INTERFACE_LANGUAGE_BUTTON)
            select = Select(select_element)
            time.sleep(1)
            select.select_by_visible_text(text)
            time.sleep(1)


    with allure.step("Заполнение поля username"):
        def fill_username_input(self, text):
            self.browser.find_element(*SettingsLocators.CHANGE_USERNAME_INPUT).send_keys(text)


    with allure.step("Получение текущего юзернейма"):
        def get_current_username(self):
            return self.get_text_from_input(*SettingsLocators.CURRENT_USERNAME)


    with allure.step("Клик на кнопку приватной политики"):
        def click_privacy_policy_button(self):
            self.click(*SettingsLocators.PRIVACY_POLICY_BUTTON)


    with allure.step("Проверка отображения текста приватной политики"):
        def check_is_privacy_policy_text_displayed(self):
            return self.browser.find_element(*SettingsLocators.PRIVACY_POLICY_TEXT).is_displayed()


    with allure.step("Получение выбранного языка для изучения"):
        def get_selected_option_for_i_learn_button(self):
            select_element = self.browser.find_element(*SettingsLocators.I_LEARN_SELECT_BUTTON)
            select = Select(select_element)
            return select.first_selected_option.text


    with allure.step("Получение выбранного родного языка"):
        def get_selected_option_for_translate_into_button(self):
            select_element = self.browser.find_element(*SettingsLocators.TRANSLATE_INTO_SELECT_BUTTON)
            select = Select(select_element)
            return select.first_selected_option.text


    with allure.step("Проверка выбранного языка интерфейса"):
        def get_selected_option_for_interface_language_button(self):
            select_element = self.browser.find_element(*SettingsLocators.INTERFACE_LANGUAGE_BUTTON)
            select = Select(select_element)
            return select.first_selected_option.text


    with allure.step("Получение текста из кнопки выхода из аккаунта"):
        def get_text_of_sign_out_button(self):
            self.scroll_to_element(*SettingsLocators.SIGN_OUT_BUTTON)
            time.sleep(1)
            return self.get_text_from_input(*SettingsLocators.SIGN_OUT_BUTTON)