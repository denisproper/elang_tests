import time

import allure
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.locators import AuthorizationLocators

class BasePage():
    def __init__(self, browser, url, timeout=3):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)


    with allure.step("Открытие страницы"):
        def open(self):
            self.browser.get(self.url)


    with allure.step("Проверка отображения элемента"):
        def is_element_present(self, how, what):
            try:
                self.browser.find_element(how, what)
            except (NoSuchElementException):
                return False
            return True


    with allure.step("Клик на элемент"):
        def click(self, how, what):
            try:
                element = WebDriverWait(self.browser, 10).until(
                    EC.element_to_be_clickable((how, what))
                )
                element.click()
            except (NoSuchElementException, TimeoutException):
                return False


    with allure.step("Получение значения из элемента"):
        def get_value_by_attribute(self, how, what):
            return self.browser.find_element(how, what).get_attribute("value")


    with allure.step("Получение текста из элемента"):
        def get_text_from_input(self, how, what):
            return self.browser.find_element(how, what).text


    with allure.step("Заполнение полей email и password"):
        def fill_email_and_password_fields(self, email, password):
            with allure.step("Заполнение email поля"):
                email_field = self.browser.find_element(*AuthorizationLocators.EMAIL_INPUT)
                email_field.clear()
                email_field.send_keys(email)

            with allure.step("Заполнение password поля"):
                password_field = self.browser.find_element(*AuthorizationLocators.PASSWORD_INPUT)
                password_field.clear()
                password_field.send_keys(password)
                self.browser.find_element(*AuthorizationLocators.LOGIN_BUTTON).click()


    def scroll_to_element(self, element):
        if element is not None:
            self.browser.execute_script("arguments[0].scrollIntoView();", element)
        else:
            raise ValueError("Element is None")


    def scroll_and_click(self, element):
        if element is not None:
            self.browser.execute_script("arguments[0].scrollIntoView(true);", element)
            time.sleep(0.5)
            element.click()
        else:
            raise ValueError("Element is None")