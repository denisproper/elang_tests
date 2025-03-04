from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class AuthorizationLocators():
    EMAIL_INPUT = (By.XPATH, "//input[@name='email']")
    PASSWORD_INPUT = (By.XPATH, "//input[@name='password']")

    WRONG_PASSWORD = (By.CSS_SELECTOR, '.ml-2.text-xs.text-red-300')
    SHORT_PASSWORD = (By.XPATH, "//div[contains(text(), 'Password must be at least 6 characters long')]")
    INVALID_EMAIL = (By.XPATH, "//div[contains(text(), 'Check that you entered your email correctly')]")
    UNAVAILABLE_ACCOUNT = (By.CSS_SELECTOR, "div.ml-2.text-xs.text-red-300")

    LOGIN_BUTTON = (By.XPATH, "//button[span[text()='Log in']]")

class SettingsLocators():
    ACCOUNT_SETTINGS_TEXT = (By.XPATH, "//div[text()='Account settings']")
    SIGN_OUT_BUTTON = (By.XPATH, "//button[contains(@class, 'bg-[#FB5353]')]")
    CHANGE_USERNAME_BUTTON = (By.XPATH, "//span[normalize-space(text())='Change username']")
    CHANGE_USERNAME_INPUT = (By.NAME, "newUsername")
    SAVE_BUTTON = (By.XPATH, "//button[span[text()='Save']]")
    CURRENT_USERNAME = (By.CSS_SELECTOR, "div.text-lg.text-gray-800.select-text.flex")
    REQUIRED_FIELD_WARNING = (By.CSS_SELECTOR, "div.ml-2.text-xs.text-red-300")
    PRIVACY_POLICY_BUTTON = (By.LINK_TEXT, "Privacy policy")
    PRIVACY_POLICY_TEXT = (By.XPATH, "//div[contains(text(), 'Privacy Policy')]")
    POINTER_TO_THE_TOP = (By.XPATH, "//img[@src='data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNjAiIGhlaWdodD0iNjAiIHZpZXdCb3g9IjAgMCA2MCA2MCIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPGNpcmNsZSBjeD0iMzAiIGN5PSIzMCIgcj0iMjkiIGZpbGw9IiNGOUZBRkIiIHN0cm9rZT0iIzlDM0ZGNSIgc3Ryb2tlLXdpZHRoPSIyIi8+CjxwYXRoIGQ9Ik0zNi4xMiAzNC41NDY5TDMwIDI4LjQ0MDJMMjMuODggMzQuNTQ2OUwyMiAzMi42NjY5TDMwIDI0LjY2NjlMMzggMzIuNjY2OUwzNi4xMiAzNC41NDY5WiIgZmlsbD0iIzlDM0ZGNSIvPgo8L3N2Zz4K']")
    I_LEARN_SELECT_BUTTON = (By.XPATH, "//select")
    TRANSLATE_INTO_SELECT_BUTTON = (By.XPATH, "(//select)[2]")
    INTERFACE_LANGUAGE_BUTTON = (By.XPATH, "(//select)[3]")



