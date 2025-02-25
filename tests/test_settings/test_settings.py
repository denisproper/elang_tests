import time
import pytest

from tests.test_authorization.check_functions import check_valid_authorization_build
from env.json_read import link, valid_email, valid_password
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
