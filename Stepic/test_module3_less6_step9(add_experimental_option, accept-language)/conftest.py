import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default="chrome",
                     help="Choose language: es or fr")


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    browser = None
    options = Options()
    if browser_name == "es":
        print("\nstart chrome browser for test..")
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        browser = webdriver.Chrome(executable_path='C:/Users/NIk/PycharmProjects/chromedriver.exe', options=options)
    elif browser_name == "fr":
        print("\nstart firefox browser for test..")
        browser = webdriver.Firefox(executable_path='C:/Users/NIk/PycharmProjects/geckodriver.exe')
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\nquit browser..")
    browser.quit()
