import pytest
from env.json_read import *
import allure

from pages.login.login_page import LoginPage


def page_build(browser, link, email, password):
    page = LoginPage(browser, link)
    page.open()
    page.fill_email_and_password_fields(email, password)
    return page


@allure.feature('Valid authorization')
def test_valid_authorization(browser):
    page = page_build(browser, link, valid_email, valid_password)
    assert page.check_valid_email_and_password_login() is True, "Что то не так"


@allure.feature('Invalid authorization')
def test_correct_email_and_wrong_password(browser):
    page = page_build(browser, link, valid_email, digits_password)
    assert page.check_wrong_password_login() is True, "Что то не так"


@allure.feature('Invalid authorization')
@pytest.mark.parametrize("email, password", [
    (valid_email, special_symbols_password),
    (digits_email, special_symbols_password),
    (digits_email_with_at_com, special_symbols_password),
    (partly_right_email, special_symbols_password),
    (digits_email_with_at, special_symbols_password)
])
def test_check_short_password(browser, email, password):
    page = page_build(browser, link, email, password)
    assert page.check_short_password_login() is True, "Что то не так"


@allure.feature('Invalid authorization')
@pytest.mark.parametrize("email, password" , [
    (digits_email, digits_password),
    (digits_email, valid_password),
    (digits_email_with_at, digits_password),
    (digits_email_with_at, valid_password)
])
def test_check_that_you_entered_your_email_correctly(browser, email, password):
    page = page_build(browser, link, email, password)
    assert page.check_invalid_email_login() is True, "Что то не так"


@allure.feature('Invalid authorization')
@pytest.mark.parametrize("email, password", [
    (digits_email_with_at_com, valid_password),  
    (digits_email_with_at_com, digits_password),
    (partly_right_email, digits_password),
    (partly_right_email, valid_password)
])
def test_couldnt_find_the_account_with_this_email_address(browser, email, password):
    page = page_build(browser, link, email, password)
    assert page.check_unavailable_account_login() is True, "Что то не так"
