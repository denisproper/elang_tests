import pytest
from selenium import webdriver
from tests.test_authorization.check_functions import check_valid_authorization_build

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()