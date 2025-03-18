import allure
import pytest

from pages.settings.support_page import SupportPage
from env.authorization.json_read import valid_password, valid_email
from env.config.json_read import link_for_vocabulary
from env.support.support_data import valid_data


@allure.feature("Test Support section")
@allure.story("Check layout")
def test_title(browser):
    page = SupportPage(browser, link_for_vocabulary)
    page.open()
    page.fill_email_and_password_fields(valid_email, valid_password)
    page.go_to_support_section()
    assert page.check_title()


@allure.feature("Test Support section")
@allure.story("Check sending message")
@pytest.mark.parametrize("name, email, message", valid_data)
def test_send_message(browser, name, email, message):
    page = SupportPage(browser, link_for_vocabulary)
    page.open()
    page.fill_email_and_password_fields(valid_email, valid_password)
    page.go_to_support_section()
    page.input_name_field(name)
    page.input_email_field(email)
    page.input_message_field(message)
    page.click_submit_button()
    assert page.check_success_message_is_displayed()

