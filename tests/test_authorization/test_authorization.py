import pytest
import allure
from env.config.json_read import *
from pages.login.login_page import LoginPage
from env.authorization.authorization_data import AuthorizationData


@allure.feature("Authorization tests")
class TestAuthorization:
    """Test suite for authorization functionality"""

    @pytest.fixture(autouse=True)
    def setup(self, browser):
        """Common setup for all tests: initialize page"""
        self.page = LoginPage(browser, link)
        self.page.open()


    def login(self, email, password):
        """Helper method to perform login with given credentials"""
        self.page.fill_email_and_password_fields(email, password)


    @allure.story("Valid authorization")
    def test_valid_authorization(self):
        """Verify successful login with valid credentials"""
        self.login(*AuthorizationData.get_valid_email_and_password_data())
        assert self.page.check_valid_email_and_password_login() is True, "Что то не так"


    @allure.story("Invalid authorization - Correct email, wrong password")
    def test_correct_email_and_wrong_password(self):
        """Verify login fails with correct email and wrong password"""
        self.login(*AuthorizationData.get_valid_email_and_wrong_password_data())
        assert self.page.check_wrong_password_login() is True, "Что то не так"


    @allure.story("Invalid authorization - Short password")
    @pytest.mark.parametrize("email, password", AuthorizationData.get_email_and_short_password_data())
    def test_check_short_password(self, email, password):
        """Verify login fails with short password"""
        self.login(email, password)
        assert self.page.check_short_password_login() is True, "Что то не так"


    @allure.story("Invalid authorization - Invalid email format")
    @pytest.mark.parametrize("email, password", AuthorizationData.get_invalid_email_format_data())
    def test_check_that_you_entered_your_email_correctly(self, email, password):
        """Verify login fails with invalid email format"""
        self.login(email, password)
        assert self.page.check_invalid_email_login() is True, "Что то не так"


    @allure.story("Invalid authorization - Account not found")
    @pytest.mark.parametrize("email, password", AuthorizationData.get_data_for_account_not_found_message())
    def test_couldnt_find_the_account_with_this_email_address(self, email, password):
        """Verify login fails when account is not found"""
        self.login(email, password)
        assert self.page.check_unavailable_account_login() is True, "Что то не так"