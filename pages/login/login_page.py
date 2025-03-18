from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from pages.locators import *

class LoginPage(BasePage): 
    def check_valid_email_and_password_login(self):
        self.browser.find_element(*AuthorizationLocators.LOGIN_BUTTON).click()
        return self.is_element_present(*SettingsLocators.ACCOUNT_SETTINGS_TEXT)
    

    def check_wrong_password_login(self):
        self.browser.find_element(*AuthorizationLocators.LOGIN_BUTTON).click()
        return self.is_element_present(*AuthorizationLocators.WRONG_PASSWORD)
    
    
    def check_short_password_login(self):
        self.browser.find_element(*AuthorizationLocators.LOGIN_BUTTON).click()
        return self.is_element_present(*AuthorizationLocators.SHORT_PASSWORD)
    
    
    def check_invalid_email_login(self):
        self.browser.find_element(*AuthorizationLocators.LOGIN_BUTTON).click()
        return self.is_element_present(*AuthorizationLocators.INVALID_EMAIL)
    
    def check_unavailable_account_login(self):
        self.browser.find_element(*AuthorizationLocators.LOGIN_BUTTON).click()
        return self.is_element_present(*AuthorizationLocators.UNAVAILABLE_ACCOUNT)
        
