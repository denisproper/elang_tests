import pytest
from check_functions import *
from env.json_read import *
import allure

@allure.feature('Valid authorization')
def test_valid_authorization(browser):
    check_valid_authorization_build(browser, link, valid_email, valid_password) 


@allure.feature('Invalid authorization')
def test_correct_email_and_wrong_password(browser):
    check_wrong_password_build(browser, link, valid_email, digits_password)


@allure.feature('Invalid authorization')
@pytest.mark.parametrize("email, password", [
    (valid_email, special_symbols_password),
    (digits_email, special_symbols_password),
    (digits_email_with_at_com, special_symbols_password),
    (partly_right_email, special_symbols_password),
    (digits_email_with_at, special_symbols_password)
])
def test_check_short_password(browser, email, password):
     check_short_password_build(browser, link, email, password)   


@allure.feature('Invalid authorization')
@pytest.mark.parametrize("email, password" , [
    (digits_email, digits_password),
    (digits_email, valid_password),
    (digits_email_with_at, digits_password),
    (digits_email_with_at, valid_password)
])
def test_check_that_you_entered_your_email_correctly(browser, email, password):
    check_that_you_entered_email_correctly(browser, link, email, password) 


@allure.feature('Invalid authorization')
@pytest.mark.parametrize("email, password", [
    (digits_email_with_at_com, valid_password),  
    (digits_email_with_at_com, digits_password),
    (partly_right_email, digits_password),
    (partly_right_email, valid_password)
])
def test_couldnt_find_the_account_with_this_email_address(browser, email, password):
    check_unavailable_account(browser, link, email, password)     
