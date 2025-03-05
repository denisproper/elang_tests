from selenium.common import StaleElementReferenceException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from pages.base_page import BasePage
from pages.locators import VocabularyLocators



class VocabularyPage(BasePage):
    def __init__(self, browser, url):
        super().__init__(browser, url)

    def go_to_vocabulary_section(self):
        self.click(*VocabularyLocators.VOCABULARY_SECTION)

    def go_to_phrases_section(self):
        self.click(*VocabularyLocators.PHRASES_SECTION)

    def check_title(self):
        return self.is_element_present(*VocabularyLocators.VOCABULARY_TITLE)

    def check_phrases_section(self):
        return self.is_element_present(*VocabularyLocators.PHRASES_SECTION)

    def check_sets_section(self):
        return self.is_element_present(*VocabularyLocators.SETS_SECTION)

    def check_words_section(self):
        return self.is_element_present(*VocabularyLocators.WORDS_SECTION)

    def input_search_field(self, text):
        self.browser.find_element(*VocabularyLocators.SEARCH_FIELD).send_keys(text)

    def get_words(self):
        try:
            elements = WebDriverWait(self.browser, 10).until(
                EC.presence_of_all_elements_located(VocabularyLocators.WORDS)
            )
            names = [el.text.strip() for el in elements]
            return names
        except StaleElementReferenceException:
            elements = self.browser.find_elements(*VocabularyLocators.WORDS)
            names = [el.text.strip() for el in elements]
            return names
        except Exception as e:
            print(f"Ошибка при получении слов: {e}")
            return []


    def get_phrases(self):
        try:
            elements = WebDriverWait(self.browser, 10).until(
                EC.presence_of_all_elements_located(VocabularyLocators.PHRASES)
            )
            bold_texts = [el.text.strip() for el in elements]
            return bold_texts
        except StaleElementReferenceException:
            elements = self.browser.find_elements(*VocabularyLocators.PHRASES)
            bold_texts = [el.text.strip() for el in elements]
            return bold_texts
        except Exception as e:
            print(f"Ошибка при получении bold текста: {e}")
            return []


    def clear_search_field(self):
        self.browser.find_element(*VocabularyLocators.SEARCH_FIELD).clear()


    def choose_sort(self, sorting_option = "A to Z"):
        self.click(*VocabularyLocators.SORT_ELEMENT)
        if sorting_option == "A to Z":
            self.click(*VocabularyLocators.A_TO_Z_SORT)
        elif sorting_option == "Z to A":
            self.click(*VocabularyLocators.Z_TO_A_SORT)
        else:
            print("Неизвестный вариант сортировки")


    def is_sorted_words(self, words: list[str], reverse = False):
        sorted_words = sorted(words, key=str.lower, reverse=reverse)
        if words == sorted_words:
            return True
        return False


