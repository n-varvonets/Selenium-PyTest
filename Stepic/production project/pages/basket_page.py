from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):

    def should_not_be_product_in_basket(self):
        # Сначала проверяем, что элементы присутствуют на странице
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), ("BASKET ITEMS is presented")

    def should_be_text_about_empty_cart(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_SMS_EMPTY), (f"Text about empty is not present")

