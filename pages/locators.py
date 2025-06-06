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
    LOGIN_BUTTON = (By.XPATH, "//button[@type='submit']")

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

class VocabularyLocators():
    VOCABULARY_TITLE = (By.XPATH, "//div[text()='Vocabulary']")
    VOCABULARY_SECTION = (By.XPATH, "//div[text()='Vocabulary']")
    PHRASES_SECTION = (By.XPATH, '//a[@href="/account/vocabulary/phares"]')
    SETS_SECTION = (By.XPATH, '//a[@href="/account/vocabulary/sets"]')
    WORDS_SECTION = (By.XPATH, '//a[@href="/account/vocabulary/words"]')
    SEARCH_FIELD = (By.ID, "search-input")
    WORDS = (By.XPATH, "//div[contains(@class, 'font-bold text-purple-20')]")
    SORT_ELEMENT = (By.CSS_SELECTOR, "label.ml-4")
    A_TO_Z_SORT = (By.XPATH, "//li[text()='A to Z']")
    Z_TO_A_SORT = (By.XPATH, "//li[text()='Z to A']")
    PHRASES = (By.XPATH, "//div[contains(@class, 'font-bold text-purple-20')]")
    CHECKBOXES = (By.CSS_SELECTOR, '.form-checkbox')
    SETTINGS_OF_SELECTED_WORDS = (By.CSS_SELECTOR, "img.cursor-pointer[alt='dots']")
    DELETE_SELECTED_WORDS_BUTTON = (By.XPATH, "//div[contains(@class, 'cursor-pointer') and contains(., 'Delete')]")
    CONFIRM_DELETE_BUTTON_FOR_WORDS = (By.XPATH, "//button[span[text()='Delete words']]")
    CONFIRM_DELETE_BUTTON_FOR_PHRASES = (By.XPATH, "//button[span[text()='Delete phrases']]")

class SupportLocators():
    SUPPORT_SECTION = (By.XPATH, "//div[text()='Support']")
    HELP_TEXT = (By.CSS_SELECTOR, "div.flex-row.active.py-5.last\\:mb-0.px-10.ts\\:px-5.ovS\\:px-5.flex.items-center")
    NAME_INPUT = (By.XPATH, "(//input[@type='text'])[1]")
    EMAIL_INPUT = (By.XPATH, "(//input[@type='text'])[2]")
    MESSAGE_INPUT = (By.XPATH, "//textarea[@name='text']")
    SUCCESSFUL_MESSAGE = (By.XPATH, "//div[@role='dialog']")
    SEND_MESSAGE_BUTTON = (By.XPATH, "//button[@type='submit']")
    INVALID_NAME_INPUT = (By.XPATH, "//span[text()='The name must be more than 1 and less than 13 symbols.']")
    INVALID_EMAIL_INPUT = (By.XPATH, "//span[text()='Enter your email in the format yourname@example.com']")
    EMPTY_MESSAGE_INPUT = (By.XPATH, "//span[text()='Please enter your message']")
    INVALID_MESSAGE_INPUT = (By.XPATH, "//span[text()='The message cannot contain less than 5 or more than 1000 symbols.']")


