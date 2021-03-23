import time

import pytest

from pages.basket_page import BasketPage
from pages.product_page import AddToBasket

# pytest -s -v -m login_guest --tb=line test_main_page.py

"""воспользуемся магией ООП уже для организации кода самих тест-кейсов.Зачем это делать и почему удобно? 
Во-первых, мы можем логически сгруппировать тесты в один класс просто ради более стройного кода:"""
@pytest.mark.login_guest
class TestLoginFromMainPage():
    # не забываем передать первым аргументом self
    def test_guest_can_go_to_login_page(self, browser):
         # реализация теста
        pass

    def test_guest_should_see_login_link(self, browser):
         # реализация теста
        pass

def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = BasketPage(browser, link)
    page.open()
    page.go_to_basket_page()
    page.should_not_be_product_in_basket()
    page.should_be_text_about_empty_cart()


def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/studyguide-for-counter-hack-reloaded_205/"
    page = BasketPage(browser, link)
    page.open()
    page.go_to_basket_page()
    page.should_not_be_product_in_basket()
    page.should_be_text_about_empty_cart()

