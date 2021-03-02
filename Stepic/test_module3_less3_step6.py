"""Если нужно проверить, что тест вызывает ожидаемое исключение (довольно редкая ситуация для UI-тестов,
и вам этот способ, скорее всего, никогда не пригодится), мы можем использовать специальную конструкцию
 with pytest.raises(). Например, можно проверить, что на странице сайта не должен отображаться какой-то элемент:"""

# for execute test=code you need to pass in terminal next cmd: pytest test_module3_less_step6.py
import pytest

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

link = "http://selenium1py.pythonanywhere.com"


def test_exception1():
    browser = webdriver.Chrome(executable_path='C:/Users/NIk/PycharmProjects/chromedriver.exe')
    try:

        browser.get(link)
        with pytest.raises(NoSuchElementException):
            browser.find_element_by_css_selector("button.btn")
            pytest.fail("Не должно быть кнопки Отправить")
    finally:
        browser.quit()


def test_exception2():
    browser = webdriver.Chrome(executable_path='C:/Users/NIk/PycharmProjects/chromedriver.exe')

    try:
        browser.get(link)
        with pytest.raises(NoSuchElementException):
            browser.find_element_by_css_selector("no_such_button.btn")
            pytest.fail("Не должно быть кнопки Отправить")
    finally:
        browser.quit()


"""В первом тесте элемент будет найден, поэтому ошибка NoSuchElementException,
которую ожидает контекстный менеджер  pytest.raises, не возникнет, и тест упадёт."""
# >>> test_3_3_9_pytest_raises.py:8 (test_exception1)
# >>> Failed: Не должно быть кнопки Отправить

"""Во втором тесте, как мы и ожидали, кнопка не будет найдена, и тест пройдет."""
#-------------------------------------------------------------------------------------------------------------
"""У кого последний pytest, там устарел параметр  message в строке with pytest.raises(NoSuchElementException,
 message="Не должно быть кнопки Отправить") - теперь так: 

with pytest.raises(NoSuchElementException):
browser.find_element_by_css_selector("button.btn")
pytest.fail("Не должно быть кнопки Отправить")"""
