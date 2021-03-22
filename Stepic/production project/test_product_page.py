import pytest
from pages.main_page import MainPage
from pages.base_page import BasePage
from pages.product_page import AddToBasket
from pages.locators import ProductPageLocators
import time


@pytest.mark.parametrize('link', [0, 1, pytest.param(7, marks=pytest.mark.xfail), 9])
def test_guest_can_add_product_to_basket(browser, link):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{link}"
    page = AddToBasket(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()                      # открываем страницу
    page.add_to_basket()             # выполняем метод страницы — переходим на страницу логина
    page.solve_quiz_and_get_code()
    page.check_methods_after_add_prod_to_cart()


def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = AddToBasket(browser,
                       link)
    page.open()
    page.add_to_basket()
    assert page.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented, but should not be"


def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = AddToBasket(browser,
                       link)
    page.open()
    assert page.is_not_element_present(
        *ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented, but should not be"


def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = AddToBasket(browser,
                       link)
    page.open()
    page.add_to_basket()
    assert page.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), 'Sucsess messege isnt disappeared'


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()


def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()

# pytest -s -v --tb=line test_product_page.py

