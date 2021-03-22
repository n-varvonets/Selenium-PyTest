import pytest
from pages.product_page import AddToBasket
from pages.locators import ProductPageLocators
import time

# product_base_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
# urls = [f"{product_base_link}/?promo=offer{no}" for no in range(10)]
# @pytest.mark.parametrize('link', urls)

# @pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
#                                   pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
#                                                "/?promo=offer7", marks=pytest.mark.xfail),
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
# def test_guest_can_add_product_to_basket(browser, link):
#     page = AddToBasket(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
#     page.open()                      # открываем страницу
#     page.add_to_basket()             # выполняем метод страницы — переходим на страницу логина
#     page.solve_quiz_and_get_code()
#     page.check_methods_after_add_prod_to_cart()

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = AddToBasket(browser,
                       link)
    page.open()
    page.add_to_basket()
    assert page.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented, but should not be"


def test_guest_cant_see_success_message(browser):
    page = AddToBasket(browser,
                       link)
    page.open()
    assert page.is_not_element_present(
        *ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented, but should not be"


def test_message_disappeared_after_adding_product_to_basket(browser):
    page = AddToBasket(browser,
                       link)
    page.open()
    page.add_to_basket()
    assert page.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), 'Sucsess messege isnt disappeared'

# pytest -s -v --tb=line test_product_page.py

