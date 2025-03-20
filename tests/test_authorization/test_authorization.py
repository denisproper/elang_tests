import pytest
import allure
from env.authorization.json_read import *
from env.config.json_read import *
from pages.login.login_page import LoginPage


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
        self.login(valid_email, valid_password)
        assert self.page.check_valid_email_and_password_login() is True, "Что то не так"


    @allure.story("Invalid authorization - Correct email, wrong password")
    def test_correct_email_and_wrong_password(self):
        """Verify login fails with correct email and wrong password"""
        self.login(valid_email, digits_password)
        assert self.page.check_wrong_password_login() is True, "Что то не так"


    @allure.story("Invalid authorization - Short password")
    @pytest.mark.parametrize("email, password", [
        (valid_email, special_symbols_password),
        (digits_email, special_symbols_password),
        (digits_email_with_at_com, special_symbols_password),
        (partly_right_email, special_symbols_password),
        (digits_email_with_at, special_symbols_password),
    ])
    def test_check_short_password(self, email, password):
        """Verify login fails with short password"""
        self.login(email, password)
        assert self.page.check_short_password_login() is True, "Что то не так"


    @allure.story("Invalid authorization - Invalid email format")
    @pytest.mark.parametrize("email, password", [
        (digits_email, digits_password),
        (digits_email, valid_password),
        (digits_email_with_at, digits_password),
        (digits_email_with_at, valid_password),
    ])
    def test_check_that_you_entered_your_email_correctly(self, email, password):
        """Verify login fails with invalid email format"""
        self.login(email, password)
        assert self.page.check_invalid_email_login() is True, "Что то не так"


    @allure.story("Invalid authorization - Account not found")
    @pytest.mark.parametrize("email, password", [
        (digits_email_with_at_com, valid_password),
        (digits_email_with_at_com, digits_password),
        (partly_right_email, digits_password),
        (partly_right_email, valid_password),
    ])
    def test_couldnt_find_the_account_with_this_email_address(self, email, password):
        """Verify login fails when account is not found"""
        self.login(email, password)
        assert self.page.check_unavailable_account_login() is True, "Что то не так"