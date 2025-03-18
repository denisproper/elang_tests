import random
import allure
from pages.settings.vocabulary_page import VocabularyPage
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
@allure.story("Проверка поиска поля ввода для слов")
def test_search_field_for_words(browser):
    page = VocabularyPage(browser, link_for_vocabulary)
    page.open()
    page.fill_email_and_password_fields(valid_email, valid_password)
    page.go_to_vocabulary_section()
    words = page.get_words()
    half_count = len(words) // 2
    random_words = random.sample(words, half_count)
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


@allure.feature("Тест Vocabulary section")
@allure.story("Проверка поиска поля ввода для фраз")
def test_search_field_for_phrases(browser):
    page = VocabularyPage(browser, link_for_vocabulary)
    page.open()
    page.fill_email_and_password_fields(valid_email, valid_password)
    page.go_to_vocabulary_section()
    page.go_to_phrases_section()
    phrases = page.get_phrases()
    print(phrases)


@allure.feature("Тест Vocabulary section")
@allure.story("Проверка удаления нескольких слов")
def test_select_and_delete_words(browser):
    page = VocabularyPage(browser, link_for_vocabulary)
    page.open()
    page.fill_email_and_password_fields(valid_email, valid_password)
    page.go_to_vocabulary_section()
    words_before_delete = page.get_words()
    checkboxes = page.get_checkboxes()
    total_checkboxes = len(checkboxes)

    if total_checkboxes == 0:
        raise ValueError("Нет доступных чекбоксов")

    if total_checkboxes == 1: half_count = 1
    else: half_count = total_checkboxes // 2

    deleted_words = words_before_delete[:half_count]

    for i in range(half_count):
        page.scroll_and_click(checkboxes[i])

    page.scroll_and_click_settings_of_selected_words()

    page.click_delete_button_for_selected_words()
    page.click_confirm_delete_button_for_words()

    words_after_delete = page.get_words()
    assert deleted_words not in words_after_delete, "Не все слова удалились"


@allure.feature("Тест Vocabulary section")
@allure.story("Проверка удаления нескольких фраз")
def test_select_and_delete_phrases(browser):
    page = VocabularyPage(browser, link_for_vocabulary)
    page.open()
    page.fill_email_and_password_fields(valid_email, valid_password)
    page.go_to_vocabulary_section()
    page.go_to_phrases_section()
    phrases_before_delete = page.get_phrases()
    checkboxes = page.get_checkboxes()
    total_checkboxes = len(checkboxes)

    if total_checkboxes == 0:
        raise ValueError("Нет доступных чекбоксов")

    half_count = total_checkboxes // 2
    deleted_words = phrases_before_delete[:half_count]

    for i in range(half_count):
        page.scroll_and_click(checkboxes[i])

    page.scroll_and_click_settings_of_selected_words()

    page.click_delete_button_for_selected_words()
    page.click_confirm_delete_button_for_phrases()

    phrases_after_delete = page.get_words()
    assert deleted_words not in phrases_after_delete, "Не все фразы удалились"

