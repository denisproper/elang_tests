from pages.login_page import LoginPage


def page_build(browser, link, email, password):
    page = LoginPage(browser, link)  
    page.open()                      
    page.fill_email_and_password_fields(email, password)
    return page
     

def check_valid_authorization_build(browser, link, email, password):
    page = page_build(browser, link,  email, password)
    assert page.check_valid_email_and_password_login() is True, "Что то не так"


def check_wrong_password_build(browser, link, email, password):
    page = page_build(browser, link,  email, password)
    assert page.check_wrong_password_login() is True, "Что то не так"


def check_short_password_build(browser, link, email, password):
    page = page_build(browser, link,  email, password)
    assert page.check_short_password_login() is True, "Что то не так"

def check_that_you_entered_email_correctly(browser, link, email, password):
    page = page_build(browser, link,  email, password)
    assert page.check_invalid_email_login() is True, "Что то не так"

def check_unavailable_account(browser, link, email, password):
    page = page_build(browser, link,  email, password)
    assert page.check_unavailable_account_login() is True, "Что то не так"
