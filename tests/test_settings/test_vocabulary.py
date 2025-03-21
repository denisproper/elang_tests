import random
import allure
import pytest
from pages.settings.vocabulary_page import VocabularyPage
from env.authorization.authorization_data import valid_email, valid_password
from env.config.json_read import link_for_vocabulary


@allure.feature("Test Vocabulary section")
class TestVocabularySection:
    """Test suite for Vocabulary section functionality"""

    @pytest.fixture(autouse=True)
    def setup(self, browser):
        """Common setup for all tests: initialize page, login, and navigate to vocabulary section"""
        self.page = VocabularyPage(browser, link_for_vocabulary)
        self.page.open()
        self.page.fill_email_and_password_fields(valid_email, valid_password)
        self.page.go_to_vocabulary_section()


    @allure.story("Check layout")
    def test_title(self):
        """Verify vocabulary section title is displayed correctly"""
        assert self.page.check_title(), "Vocabulary section title is not displayed correctly"


    @allure.story("Check vocabulary sections")
    def test_sections(self):
        """Verify all vocabulary sections (words, phrases, sets) are displayed"""
        assert self.page.check_words_section(), "Words section is not displayed"
        assert self.page.check_phrases_section(), "Phrases section is not displayed"
        assert self.page.check_sets_section(), "Sets section is not displayed"


    @allure.story("Check search field for words")
    def test_search_field_for_words(self):
        """Verify search functionality for words"""
        words = self.page.get_words()
        if not words:
            assert words == []
            return
        half_count = len(words) // 2
        random_words = random.sample(words, half_count)
        for word in random_words:
            self.page.input_search_field(word)
            assert word in self.page.get_words(), f"Word '{word}' is not displayed in search results"
            self.page.clear_search_field()


    @allure.story("Check sorting functionality")
    def test_sort(self):
        """Verify sorting of words in ascending and descending order"""
        words_ascending = self.page.get_words()
        if not words_ascending:
            assert words_ascending == []
            return
        self.page.choose_sort("A to Z")
        assert self.page.is_sorted_words(words_ascending), "Words are not sorted from A to Z"

        self.page.choose_sort("Z to A")
        words_descending = self.page.get_words()
        assert self.page.is_sorted_words(words_descending, reverse=True), "Words are not sorted from Z to A"


    @allure.story("Check search field for phrases")
    def test_search_field_for_phrases(self):
        """Verify search field visibility and functionality for phrases"""
        phrases = self.page.get_phrases()
        if not phrases:
            assert phrases == []
            return
        half_count = len(phrases) // 2
        random_phrases = random.sample(phrases, half_count)
        for phrase in random_phrases:
            self.page.input_search_field(phrase)
            assert phrase in self.page.get_words(), f"Word '{phrase}' is not displayed in search results"
            self.page.clear_search_field()


    @allure.story("Check deletion of multiple words")
    def test_select_and_delete_words(self):
        """Verify deletion of multiple selected words"""
        words_before_delete = self.page.get_words()
        if not words_before_delete:
            assert words_before_delete == []
            return
        checkboxes = self.page.get_checkboxes()
        total_checkboxes = len(checkboxes)

        if total_checkboxes == 0:
            raise ValueError("No available checkboxes to select")

        half_count = 1 if total_checkboxes == 1 else total_checkboxes // 2
        deleted_words = words_before_delete[:half_count]

        for i in range(half_count):
            self.page.scroll_and_click(checkboxes[i])

        self.page.scroll_and_click_settings_of_selected_words()
        self.page.click_delete_button_for_selected_words()
        self.page.click_confirm_delete_button_for_words()

        words_after_delete = self.page.get_words()
        for word in deleted_words:
            assert word not in words_after_delete, f"Word '{word}' was not deleted"


    @allure.story("Check deletion of multiple phrases")
    def test_select_and_delete_phrases(self):
        """Verify deletion of multiple selected phrases"""
        self.page.go_to_phrases_section()
        phrases_before_delete = self.page.get_phrases()
        if not phrases_before_delete:
            assert phrases_before_delete == []
            return
        checkboxes = self.page.get_checkboxes()
        total_checkboxes = len(checkboxes)

        if total_checkboxes == 0:
            raise ValueError("No available checkboxes to select")

        half_count = 1 if total_checkboxes == 1 else total_checkboxes // 2
        deleted_phrases = phrases_before_delete[:half_count]

        for i in range(half_count):
            self.page.scroll_and_click(checkboxes[i])

        self.page.scroll_and_click_settings_of_selected_words()
        self.page.click_delete_button_for_selected_words()
        self.page.click_confirm_delete_button_for_phrases()

        phrases_after_delete = self.page.get_phrases()
        for phrase in deleted_phrases:
            assert phrase not in phrases_after_delete, f"Phrase '{phrase}' was not deleted"

