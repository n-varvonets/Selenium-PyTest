"""Когда тестов становится много, хорошо иметь способ разделять тесты не только по названиям, но также по каким-нибудь
заданным нами категориям.
Например, мы можем выбрать небольшое количество критичных тестов (smoke), которые нужно запускать на каждый коммит
разработчиков, а остальные тесты обозначить как регрессионные (regression) и запускать их только перед релизом. Или у
нас могут быть тесты, специфичные для конкретного браузера (internet explorer 11), и мы хотим запускать эти тесты только
под данный браузер. Для выборочного запуска таких тестов в PyTest используется маркировка тестов или метки (marks).
Для маркировки теста нужно написать декоратор вида @pytest.mark.mark_name"""

import pytest
from selenium import webdriver

link = "http://selenium1py.pythonanywhere.com/"


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome(executable_path='C:/Users/NIk/PycharmProjects/chromedriver.exe')
    yield browser
    print("\nquit browser..")
    browser.quit()


class TestMainPage1():

    @pytest.mark.smoke
    def test_guest_should_see_login_link(self, browser):
        browser.get(link)
        browser.find_element_by_css_selector("#login_link")

    @pytest.mark.regression
    def test_guest_should_see_basket_link_on_the_main_page(self, browser):
        browser.get(link)
        browser.find_element_by_css_selector(".basket-mini .btn-group > a")

# pytest -s -v -m smoke test_module3_less5_step2.py - запустить тест с нужной маркировкой нужно -m и нужную метку
# pytest -s -v -m "not smoke" test_fixture8.py  - чтобы запустить все тесты, не имеющие заданную маркировку
# pytest -s -v -m "smoke or regression" test_fixture8.py - для запуска тестов с разными метками


"""Это предупреждение появилось потому, что в последних версиях PyTest настоятельно
рекомендуется регистрировать метки явно перед использованием

Как же регистрировать метки?
Создайте файл pytest.ini в корневой директории вашего тестового проекта и добавьте в файл следующие строки:

[pytest]
markers =
    smoke: marker for smoke tests
    regression: marker for regression tests"""


