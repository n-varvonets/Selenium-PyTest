import pytest
from pages.main_page import MainPage
from pages.base_page import BasePage
from pages.product_page import AddToBasket
from pages.locators import ProductPageLocators
from pages.login_page import LoginPage
from pages.basket_page import BasketPage
import time

# pytest -s -v --tb=line test_product_page.py - cmd for running tests


# class TestUserAddToBasketFromProductPage:
#     @pytest.fixture(scope="function", autouse=True)
#     def setup(self, browser):
#         email = str(time.time()) + "@fakemail.org"
#         password = "QQQqqq111"
#         link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
#         self.page = LoginPage(browser, link)
#         self.page.open()
#         self.page.go_to_login_page()
#         self.page.register_new_user(email, password)
#         self.page.should_be_authorized_user()
#         self.page = LoginPage(browser, link)
#         self.page.open()
#
#     # 1)test_user_can_add_product_to_basket
#     def test_user_can_add_product_to_basket(self, browser):
#         self.page.add_to_basket()
#         assert self.page.is_element_present(
#             *ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented, but should not be"

class TestGuestGoToLoginPage:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-shellcoders-handbook_209/"
        self.page = BasketPage(browser, link)
        self.page.open()

    # 2)test_guest_can_add_product_to_basket
    # def test_guest_can_add_product_to_basket(self):
    #     self.page.add_to_basket()
    #     assert self.page.is_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Guest can add product to basket, but he should"

    # 3)test_guest_cant_see_product_in_basket_opened_from_product_page
    def test_guest_cant_see_product_in_basket_opened_from_product_page(self):
        self.page.go_to_basket_page()

        assert self.page.should_be_text_about_empty_cart(), "Product in basket, but should not be"

# 4)test_guest_can_go_to_login_page_from_product_page
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-shellcoders-handbook_209/"
    page = LoginPage(browser, link)
    page.open()
    page.go_to_login_page()
    assert page.should_be_login_page()

















"""It's ONLY for me, not for checking"""
# @pytest.mark.parametrize('link', [0, 1, pytest.param(7, marks=pytest.mark.xfail), 9])
# def test_guest_can_add_product_to_basket(browser, link):
#     link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{link}"
#     page = AddToBasket(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
#     page.open()                      # открываем страницу
#     page.add_to_basket()             # выполняем метод страницы — переходим на страницу логина
#     page.solve_quiz_and_get_code()
#     page.check_methods_after_add_prod_to_cart()


