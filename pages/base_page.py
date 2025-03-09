import time

import allure
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from pages.locators import AuthorizationLocators

class BasePage():
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.wait = WebDriverWait(self.browser, timeout, poll_frequency=1)


    @allure.step("Открытие страницы")
    def open(self):
        self.browser.get(self.url)


    @allure.step("Проверка отображения элемента")
    def is_element_present(self, how, what):
        try:
            self.wait.until(EC.presence_of_element_located((how, what)))
            return True
        except TimeoutException:
            return False


    @allure.step("Клик на элемент")
    def click(self, how, what):
        try:
            element = self.wait.until(EC.element_to_be_clickable((how, what)))
            element.click()
        except TimeoutException:
            raise TimeoutException(f"Не удалось кликнуть по элементу {what}")


    @allure.step("Получение значения из элемента")
    def get_value_by_attribute(self, how, what, attribute="value"):
        element = self.wait.until(EC.presence_of_element_located((how, what)))
        return element.get_attribute(attribute)


    @allure.step("Получение текста из элемента")
    def get_text_from_input(self, how, what):
        element = self.wait.until(EC.presence_of_element_located((how, what)))
        return element.text


    @allure.step("Заполнение полей email и password")
    def fill_email_and_password_fields(self, email, password):
        email_field = self.wait.until(EC.visibility_of_element_located(AuthorizationLocators.EMAIL_INPUT))
        email_field.clear()
        email_field.send_keys(email)

        password_field = self.wait.until(EC.visibility_of_element_located(AuthorizationLocators.PASSWORD_INPUT))
        password_field.clear()
        password_field.send_keys(password)

        login_button = self.wait.until(EC.element_to_be_clickable(AuthorizationLocators.LOGIN_BUTTON))
        login_button.click()


    def scroll_to_element(self, how, what):
        element = self.wait.until(EC.presence_of_element_located((how, what)))
        self.browser.execute_script("arguments[0].scrollIntoView();", element)


    def scroll_and_click(self, how, what):
        element = self.wait.until(EC.element_to_be_clickable((how, what)))
        self.browser.execute_script("arguments[0].scrollIntoView(true);", element)
        time.sleep(0.5)
        element.click()
