from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class AuthorizationLocators():
    EMAIL_INPUT = (By.XPATH, "//input[@name='email']")
    PASSWORD_INPUT = (By.XPATH, "//input[@name='password']")

    WRONG_PASSWROD = (By.CSS_SELECTOR,'.ml-2.text-xs.text-red-300')
    SHORT_PASSWORD = (By.XPATH, "//div[contains(text(), 'Password must be at least 6 characters long')]")
    INVALID_EMAIL = (By.XPATH, "//div[contains(text(), 'Check that you entered your email correctly')]")
    UNAVAILABLE_ACCOUNT = (By.CSS_SELECTOR, "div.ml-2.text-xs.text-red-300")

    LOGIN_BUTTON = (By.XPATH, "//button[span[text()='Log in']]")

class SettingsLocatots():
    AccountSettingsText = (By.XPATH, "//div[text()='Account settings']")