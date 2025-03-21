from selenium.common import StaleElementReferenceException, ElementNotInteractableException
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage
from pages.locators import VocabularyLocators


class VocabularyPage(BasePage):
    def __init__(self, browser, url):
        super().__init__(browser, url)

    def go_to_vocabulary_section(self):
        self.wait.until(EC.element_to_be_clickable(VocabularyLocators.VOCABULARY_SECTION)).click()

    def go_to_phrases_section(self):
        self.wait.until(EC.element_to_be_clickable(VocabularyLocators.PHRASES_SECTION)).click()

    def check_title(self):
        return self.wait.until(EC.presence_of_element_located(VocabularyLocators.VOCABULARY_TITLE))

    def check_phrases_section(self):
        return self.wait.until(EC.presence_of_element_located(VocabularyLocators.PHRASES_SECTION))

    def check_sets_section(self):
        return self.wait.until(EC.presence_of_element_located(VocabularyLocators.SETS_SECTION))

    def check_words_section(self):
        return self.wait.until(EC.presence_of_element_located(VocabularyLocators.WORDS_SECTION))

    def input_search_field(self, text):
        search_field = self.wait.until(EC.presence_of_element_located(VocabularyLocators.SEARCH_FIELD))
        search_field.send_keys(text)

    def get_words(self):
        try:
            elements = self.wait.until(EC.presence_of_all_elements_located(VocabularyLocators.WORDS))
            return [el.text.strip() for el in elements]
        except StaleElementReferenceException:
            elements = self.browser.find_elements(*VocabularyLocators.WORDS)
            return [el.text.strip() for el in elements]
        except Exception as e:
            return []

    def get_phrases(self):
        try:
            elements = self.wait.until(EC.presence_of_all_elements_located(VocabularyLocators.PHRASES))
            return [el.text.strip() for el in elements]
        except StaleElementReferenceException:
            elements = self.browser.find_elements(*VocabularyLocators.PHRASES)
            return [el.text.strip() for el in elements]
        except Exception as e:
            return []

    def clear_search_field(self):
        search_field = self.wait.until(EC.presence_of_element_located(VocabularyLocators.SEARCH_FIELD))
        search_field.clear()

    def choose_sort(self, sorting_option="A to Z"):
        self.wait.until(EC.element_to_be_clickable(VocabularyLocators.SORT_ELEMENT)).click()
        if sorting_option == "A to Z":
            self.wait.until(EC.element_to_be_clickable(VocabularyLocators.A_TO_Z_SORT)).click()
        elif sorting_option == "Z to A":
            self.wait.until(EC.element_to_be_clickable(VocabularyLocators.Z_TO_A_SORT)).click()
        else:
            print("Неизвестный вариант сортировки")

    def is_sorted_words(self, words: list[str], reverse=False):
        return words == sorted(words, key=str.lower, reverse=reverse)

    def get_checkboxes(self):
        return self.wait.until(EC.visibility_of_all_elements_located(VocabularyLocators.CHECKBOXES))

    def scroll_and_click_settings_of_selected_words(self):
        element = self.wait.until(EC.element_to_be_clickable(VocabularyLocators.SETTINGS_OF_SELECTED_WORDS))
        self.scroll_and_click(element)

    def click_delete_button_for_selected_words(self):
        self.wait.until(EC.element_to_be_clickable(VocabularyLocators.DELETE_SELECTED_WORDS_BUTTON)).click()

    def click_confirm_delete_button_for_words(self):
        self.wait.until(EC.element_to_be_clickable(VocabularyLocators.CONFIRM_DELETE_BUTTON_FOR_WORDS)).click()

    def click_confirm_delete_button_for_phrases(self):
        self.wait.until(EC.element_to_be_clickable(VocabularyLocators.CONFIRM_DELETE_BUTTON_FOR_PHRASES)).click()
