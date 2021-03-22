from .base_page import BasePage
from .locators import ProductPageLocators


class AddToBasket(BasePage):
    def check_methods_after_add_prod_to_cart(self):
        self.should_be_message_about_adding()
        self.should_be_message_basket_total()

    def add_to_basket(self):
        self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET).click()

    def should_be_message_about_adding(self):
        # Сначала проверяем, что элементы присутствуют на странице
        assert self.is_element_present(*ProductPageLocators.PRODUCT_NAME), ("Product name is not presented")
        assert self.is_element_present(*ProductPageLocators.MESSAGE_ABOUT_ADDING), ("Message about adding is not presented")
        # Затем получаем текст элементов для проверки
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text  # >>> The shellcoder's handbook
        message = self.browser.find_element(*ProductPageLocators.MESSAGE_ABOUT_ADDING).text  # >>> The shellcoder's handbook был добавлен в вашу корзину.(без strong)
        # Проверяем, что название товара присутствует в сообщении о добавлении
        # Это можно было бы сделать с помощью split() и сравнения строк, но не вижу необходимости усложнять код
        # print(product_name, "product_name and", message, "message") >>> The shellcoder's handbook product_name and The shellcoder's handbook был добавлен в вашу корзину. message
        assert product_name == message, f"No product name({product_name}) in the message({message})"

    def should_be_message_basket_total(self):
        # Сначала проверяем, что элементы присутствуют на странице
        assert self.is_element_present(*ProductPageLocators.MESSAGE_BASKET_TOTAL), (
            "Message basket total is not presented")
        assert self.is_element_present(*ProductPageLocators.PRODUCT_PRICE), (
            "Product price is not presented")
        # Затем получаем текст элементов для проверки
        message_basket_total = self.browser.find_element(*ProductPageLocators.MESSAGE_BASKET_TOTAL).text
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        # Проверяем, что цена товара присутствует в сообщении со стоимостью корзины
        # print(message_basket_total, "message_basket_total and", product_price, "product_price") >>>9,99 £ message_basket_total and 9,99 £ product_price
        assert product_price in message_basket_total, "No product price in the message"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_dissapear_of_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

