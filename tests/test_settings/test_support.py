import allure
import pytest
from pages.settings.support_page import SupportPage
from env.authorization.authorization_data import valid_email, valid_password
from env.config.json_read import link_for_vocabulary
from env.support.support_data import SupportData


@allure.feature("Test Support section")
class TestSupportSection:
    """Test suite for Support section functionality"""

    @pytest.fixture(autouse=True)
    def setup(self, browser):
        """Common setup for all tests: initialize page and login"""
        self.page = SupportPage(browser, link_for_vocabulary)
        self.page.open()
        self.page.fill_email_and_password_fields(valid_email, valid_password)
        self.page.go_to_support_section()


    @allure.story("Check layout")
    def test_title(self):
        """Verify support section title is displayed correctly"""
        assert self.page.check_title(), "Support section title is not displayed correctly"


    @allure.story("Check sending message with valid data")
    @pytest.mark.parametrize("name, email, message", SupportData.get_valid_data())
    def test_send_message_with_valid_data(self, name, email, message):
        """Verify message sending functionality with valid data"""
        self.page.input_name_field(name)
        self.page.input_email_field(email)
        self.page.input_message_field(message)
        self.page.click_submit_button()
        assert self.page.check_success_message_is_displayed(), "Success message not displayed after sending"


    @allure.story("Check sending message with invalid name data")
    @pytest.mark.parametrize("name, email, message", SupportData.get_invalid_name_data())
    def test_send_message_with_invalid_name(self, name, email, message):
        """Verify message sending functionality with valid data"""
        self.page.input_name_field(name)
        self.page.input_email_field(email)
        self.page.input_message_field(message)
        assert self.page.check_invalid_name_message_is_displayed(), "Message about entering invalid name is not displayed"


    @allure.story("Check sending message with invalid email data")
    @pytest.mark.parametrize("name, email, message", SupportData.get_invalid_email_data())
    def test_send_message_with_invalid_email(self, name, email, message):
        """Verify message sending functionality with valid data"""
        self.page.input_name_field(name)
        self.page.input_email_field(email)
        self.page.input_message_field(message)
        assert self.page.check_invalid_email_message_is_displayed(), "Message about entering invalid email is not displayed"

    @allure.story("Check sending message with empty message")
    @pytest.mark.parametrize("name, email, message", SupportData.get_empty_message_data())
    def test_send_message_with_empty_message(self, name, email, message):
        """Verify message sending functionality with valid data"""
        self.page.input_name_field(name)
        self.page.input_email_field(email)
        self.page.input_message_field(message)
        assert self.page.check_empty_sentence_message_is_displayed(), "Message about entering empty message is not displayed"


    @allure.story("Check sending message with invalid message")
    @pytest.mark.parametrize("name, email, message", SupportData.get_invalid_message_data())
    def test_send_message_with_invalid_message(self, name, email, message):
        """Verify message sending functionality with valid data"""
        self.page.input_name_field(name)
        self.page.input_email_field(email)
        self.page.input_message_field(message)
        assert self.page.check_invalid_sentence_message_is_displayed(), "Message about entering invalid message is not displayed"
