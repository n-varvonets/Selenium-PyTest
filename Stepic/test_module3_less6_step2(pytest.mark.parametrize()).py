"""PyTest позволяет запустить один и тот же тест с разными входными параметрами.
Для этого используется декоратор @pytest.mark.parametrize().
Обратите внимание, что внутри декоратора имя параметра оборачивается в кавычки, а в списке аргументов теста кавычки не нужны."""

import pytest
from selenium import webdriver
import time

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome(executable_path='C:/Users/NIk/PycharmProjects/chromedriver.exe')
    yield browser
    print("\nquit browser..")
    browser.quit()

@pytest.mark.parametrize('language', ["ru", "en-gb"])
def test_guest_should_see_login_link(browser, language):
    link = f"http://selenium1py.pythonanywhere.com/{language}/"
    browser.get(link)
    time.sleep(5)
    browser.find_element_by_css_selector("#login_link")


# pytest -s -v test_module3_less6_step2.py