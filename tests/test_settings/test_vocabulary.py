import time
import random
import allure

from pages.vocabulary_page import VocabularyPage
from env.json_read import link_for_vocabulary, valid_password, valid_email


@allure.feature("Тест Vocabulary section")
@allure.story("Проверка названия")
def test_title(browser):
    page = VocabularyPage(browser, link_for_vocabulary)
    page.open()
    page.fill_email_and_password_fields(valid_email, valid_password)
    page.go_to_vocabulary_section()
    assert page.check_title()


@allure.feature("Тест Vocabulary section")
@allure.story("Проверка разделов словаря")
def test_sections(browser):
    page = VocabularyPage(browser, link_for_vocabulary)
    page.open()
    page.fill_email_and_password_fields(valid_email, valid_password)
    page.go_to_vocabulary_section()
    assert page.check_words_section()
    assert page.check_phrases_section()
    assert page.check_sets_section()


@allure.feature("Тест Vocabulary section")
@allure.story("Проверка поиска поля ввода")
def test_search_field(browser):
    page = VocabularyPage(browser, link_for_vocabulary)
    page.open()
    page.fill_email_and_password_fields(valid_email, valid_password)
    page.go_to_vocabulary_section()
    words = page.get_words()
    random_words = random.sample(words, 5)
    for word in random_words:
        page.input_search_field(word)
        assert word in page.get_words(), f"Слово '{word}' не отображается в результатах поиска"
        page.clear_search_field()


@allure.feature("Тест Vocabulary section")
@allure.story("Проверка сортировки поля ввода")
def test_sort(browser):
    page = VocabularyPage(browser, link_for_vocabulary)
    page.open()
    page.fill_email_and_password_fields(valid_email, valid_password)
    page.go_to_vocabulary_section()
    page.choose_sort("A to Z")
    words_ascending = page.get_words()
    assert page.is_sorted_words(words_ascending)

    page.choose_sort("Z to A")
    words_descending = page.get_words()
    assert page.is_sorted_words(words_descending, reverse=True)