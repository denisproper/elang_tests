import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture(scope="function")
def browser():
    options = Options()
    options.add_argument("--window-size=1920, 1080")
    options.add_argument("--headless")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.3")
    print("\nstart browser for test..")
    browser = webdriver.Chrome(options=options)
    browser.maximize_window()
    yield browser
    print("\nquit browser..")
    time.sleep(20)
    browser.quit()

