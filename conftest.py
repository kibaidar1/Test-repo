import pytest
from selenium import webdriver
from selenium.webdriver.opera.options import Options as opera_options
from selenium.webdriver.chrome.options import Options as chrome_options


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='chrome',
                     help="Choose browser: chrome or opera")
    parser.addoption('--language', action='store', default='en',
                     help="Choose language: en or ru or ...")


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    user_language = request.config.getoption("language")
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        options = chrome_options()
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        browser = webdriver.Chrome(options=options)
    elif browser_name == "opera":
        print("\nstart opera browser for test..")
        options = opera_options()
        options.binary_location = r'C:\Programs\Opera\opera.exe'
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        browser = webdriver.Opera(options=options)
    else:
        raise pytest.UsageError("--browser_name should be chrome or opera")
    yield browser
    print("\nquit browser..")
    browser.quit()
