from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import *

class LoginPage(BasePage): 
    def fill_email_and_password_fields(self, email, password):
        email_field = self.browser.find_element(*AuthorizationLocators.EMAIL_INPUT)
        email_field.clear()
        email_field.send_keys(email)

        password_field = self.browser.find_element(*AuthorizationLocators.PASSWORD_INPUT)
        password_field.clear()
        password_field.send_keys(password)

    def check_valid_email_and_password_login(self):
        self.browser.find_element(*AuthorizationLocators.LOGIN_BUTTON).click()
        return self.is_element_present(*SettingsLocatots.AccountSettingsText)
    

    def check_wrong_password_login(self):
        self.browser.find_element(*AuthorizationLocators.LOGIN_BUTTON).click()
        return self.is_element_present(*AuthorizationLocators.WRONG_PASSWROD)
    
    
    def check_short_password_login(self):
        self.browser.find_element(*AuthorizationLocators.LOGIN_BUTTON).click()
        return self.is_element_present(*AuthorizationLocators.SHORT_PASSWORD)
    
    
    def check_invalid_email_login(self):
        self.browser.find_element(*AuthorizationLocators.LOGIN_BUTTON).click()
        return self.is_element_present(*AuthorizationLocators.INVALID_EMAIL)
    
    def check_unavailable_account_login(self):
        self.browser.find_element(*AuthorizationLocators.LOGIN_BUTTON).click()
        return self.is_element_present(*AuthorizationLocators.UNAVAILABLE_ACCOUNT)
        
