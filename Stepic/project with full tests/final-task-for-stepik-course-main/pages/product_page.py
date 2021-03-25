from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def add_product_to_basket(self):
        basket_link = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        basket_link.click()

    def should_be_basket_button(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET_BUTTON), 'There is no add to basket button'

    def basket_price_should_be_correct(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        product_price_text=product_price.text
        basket_price = self.browser.find_element(*ProductPageLocators.BASKET_PRICE)
        basket_price_text = basket_price.text
        assert product_price_text == basket_price_text, 'Price in basket is not correct!'

    def book_name_in_basket_should_be_correct(self):
        basket_book_name = self.browser.find_element(*ProductPageLocators.BASKET_BOOK_NAME)
        basket_book_name_text = basket_book_name.text
        book_name = self.browser.find_element(*ProductPageLocators.BOOK_NAME)
        book_name_text = book_name.text
        assert book_name_text == basket_book_name_text, "Book's name in basket is not correct"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented, but should not be"

    def should_be_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), 'Element is not disappeared, but should be'









