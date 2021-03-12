import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chrome",
                     help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default="en",
                     help="Choose language: es or fr")


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    user_language = request.config.getoption("language")
    browser = None
    if browser_name == "chrome":
        print(f"\nstart chrome browser for test with {user_language} language..")
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        browser = webdriver.Chrome(executable_path="C:/Users/NIk/PycharmProjects/chromedriver.exe",
                                   options=options)
    elif browser_name == "firefox":
        print(f"\nstart firefox browser for test with {user_language} language..")
        fp = webdriver.FirefoxProfile()
        fp.set_preference("intl.accept_languages", user_language)
        browser = webdriver.Firefox(executable_path='C:/Users/NIk/PycharmProjects/geckodriver.exe',
                                    firefox_profile=fp)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    browser.maximize_window()
    yield browser
    print("\nquit browser..")
    browser.quit()
