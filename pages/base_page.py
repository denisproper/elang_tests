from selenium.common.exceptions import NoSuchElementException

from pages.locators import AuthorizationLocators

class BasePage():
    def __init__(self, browser, url, timeout=3):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException):
            return False
        return True
    
    def click(self, how, what):
        try:
            self.browser.find_element(how, what).click()
        except (NoSuchElementException):
            return False
    
    def get_value_by_attribute(self, how, what):
        return self.browser.find_element(how, what).get_attribute("value")
    
    def get_text_from_input(self, how, what):
        return self.browser.find_element(how, what).text
    
    def fill_email_and_password_fields(self, email, password):
        email_field = self.browser.find_element(*AuthorizationLocators.EMAIL_INPUT)
        email_field.clear()
        email_field.send_keys(email)

        password_field = self.browser.find_element(*AuthorizationLocators.PASSWORD_INPUT)
        password_field.clear()
        password_field.send_keys(password)
        self.browser.find_element(*AuthorizationLocators.LOGIN_BUTTON).click()
