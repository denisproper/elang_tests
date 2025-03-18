import allure

from pages.settings.support_page import SupportPage
from env.json_read import link_for_vocabulary, valid_password, valid_email


@allure.feature("Test Support section")
@allure.feature("Check layout")
def test_title(browser):
    page = SupportPage(browser, link_for_vocabulary)
    page.open()
    page.fill_email_and_password_fields(valid_email, valid_password)
    page.go_to_support_section()
    assert page.check_title()