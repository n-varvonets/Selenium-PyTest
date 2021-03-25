from .base_page import BasePage
from .locators import BasePageLocators

class BasketPage(BasePage):
    def should_be_message_basket_empty(self):
        assert self.is_element_present(*BasePageLocators.BASKET_EMPTY_MESSAGE), 'Basket is not empty message is presented'

    def should_not_be_message_basket_is_empty(self):
        assert self.is_not_element_present(*BasePageLocators.BASKET_EMPTY_MESSAGE), 'Basket is empty message is presented, but should not be'

    def should_not_be_products_in_basket(self):
        assert self.is_not_element_present(*BasePageLocators.PRODUCTS_IN_BASKET), 'Products is in the basket, but should not be'
