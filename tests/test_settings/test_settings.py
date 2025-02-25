import time
import pytest

from tests.test_authorization.check_functions import check_valid_authorization_build
from env.json_read import link, valid_email, valid_password, link_for_privacy_policy
from pages.settings_page import SettingsPage
from env.json_read import link_for_settings

def page_build(browser):
    page = SettingsPage(browser, link_for_settings)  
    page.open()                      
    return page


def test_is_sign_out_button_present(browser):
    page = page_build(browser)
    page.fill_email_and_password_fields(valid_email, valid_password)
    page.check_sign_out_button()


@pytest.mark.parametrize("input", [
    "12345678", 
    "denis",
    "...", 
    " "
])
def test_change_username(browser, input):
    page = page_build(browser)
    page.fill_email_and_password_fields(valid_email, valid_password)
    page.click_change_username()
    page.fill_username_input(input)
    page.click_save_button()
    time.sleep(1)
    print(page.get_current_username())
    if input == " ":
        assert page.get_current_username() == "", "введенные имена не равны"
    else:
        assert page.get_current_username() == input, "введенные имена не равны"


def test_required_field_warning(browser):
    page = page_build(browser)
    page.fill_email_and_password_fields(valid_email, valid_password)
    page.click_change_username()
    page.fill_username_input("")
    page.click_save_button()
    page.check_required_field()


def test_privacy_policy(browser):
    page = page_build(browser)
    page.fill_email_and_password_fields(valid_email, valid_password)
    page.click_privacy_policy_button()
    windows = browser.window_handles
    browser.switch_to.window(windows[-1])
    page.check_is_privacy_policy_present()
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)
    page.click_pointer_to_the_top()
    time.sleep(2)
    page.check_is_privacy_policy_text_displayed()
    assert browser.current_url == link_for_privacy_policy


@pytest.mark.parametrize("input", [
    "Bulgarian", 
    "English",
    "Russian", 
])
def test_select_i_learn_button(browser, input):
    page = page_build(browser)
    page.fill_email_and_password_fields(valid_email, valid_password)
    page.select_language_of_i_learn_button(input)
    assert page.get_selected_option_for_i_learn_button() == input, "Языки не совпадают"


@pytest.mark.parametrize("input", [
    "Serbian", 
    "Afrikaans",
    "Zulu", 
])
def test_translate_into_button(browser, input):
    page = page_build(browser)
    page.fill_email_and_password_fields(valid_email, valid_password)
    page.select_language_of_translate_into_button(input)
    assert page.get_selected_option_for_i_learn_button() == input, "Языки не совпадают"