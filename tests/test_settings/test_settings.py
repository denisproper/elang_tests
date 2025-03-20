import time
import allure
import pytest
from env.authorization.json_read import valid_email, valid_password
from env.config.json_read import link_for_privacy_policy, link_for_settings
from pages.settings.settings_page import SettingsPage


@allure.feature("Test Settings section")
class TestSettingsSection:
    """Test suite for Settings section functionality"""

    @pytest.fixture(autouse=True)
    def setup(self, browser):
        """Common setup for all tests: initialize page and login"""
        self.page = SettingsPage(browser, link_for_settings)
        self.page.open()
        self.page.fill_email_and_password_fields(valid_email, valid_password)
        self.browser = browser


    @allure.story("Check sign out button visibility")
    def test_is_sign_out_button_present(self):
        """Verify that the sign out button is present"""
        self.page.check_sign_out_button()


    @allure.story("Check username change functionality")
    @pytest.mark.parametrize("input", [
        "12345678",
        "denis",
        "...",
        " ",
    ])
    def test_change_username(self, input):
        """Verify changing username with various inputs"""
        self.page.click_change_username()
        self.page.fill_username_input(input)
        self.page.click_save_button()
        time.sleep(1)
        current_username = self.page.get_current_username()
        if input == " ":
            assert current_username == "", "введенные имена не равны"
        else:
            print(current_username, input)
            assert current_username == input, "введенные имена не равны"


    @allure.story("Check warning for empty username")
    def test_required_field_warning(self):
        """Verify warning message appears when username is empty"""
        self.page.click_change_username()
        self.page.fill_username_input("")
        self.page.click_save_button()
        self.page.check_required_field()


    @allure.story("Check privacy policy page")
    def test_privacy_policy(self):
        """Verify privacy policy page loads and functions correctly"""
        self.page.click_privacy_policy_button()
        windows = self.browser.window_handles
        self.browser.switch_to.window(windows[-1])
        self.page.check_is_privacy_policy_present()
        self.browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)
        self.page.click_pointer_to_the_top()
        time.sleep(2)
        self.page.check_is_privacy_policy_text_displayed()
        assert self.browser.current_url == link_for_privacy_policy, \
            f"Expected URL '{link_for_privacy_policy}', got '{self.browser.current_url}'"


    @allure.story("Check selection of learning languages")
    @pytest.mark.parametrize("input", [
        "Bulgarian",
        "English",
        "Russian",
    ])
    def test_select_i_learn_button(self, input):
        """Verify selection of languages to learn"""
        self.page.select_language_of_i_learn_button(input)
        assert self.page.get_selected_option_for_i_learn_button() == input, "Языки не совпадают"


    @allure.story("Check selection of native languages")
    @pytest.mark.parametrize("input", [
        "Serbian",
        "Afrikaans",
        "Zulu",
    ])
    def test_translate_into_button(self, input):
        """Verify selection of languages to translate into"""
        self.page.select_language_of_translate_into_button(input)
        assert self.page.get_selected_option_for_translate_into_button() == input, "Языки не совпадают"


    @allure.story("Check selection of interface languages")
    @pytest.mark.parametrize("input", [
        "Russian",
        "English",
        "German",
    ])
    def test_interface_language_button(self, input):
        """Verify selection of interface languages"""
        self.page.select_language_of_interface_button(input)
        if input == "Russian":
            assert self.page.get_selected_option_for_interface_language_button() == "Русский", "Языки не совпадают"
            assert self.page.get_text_of_sign_out_button() == "Выйти из аккаунта", \
                "Sign out button text does not match expected Russian translation"
        else:
            assert self.page.get_selected_option_for_interface_language_button() == input, "Языки не совпадают"