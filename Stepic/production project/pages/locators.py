from selenium.webdriver.common.by import By


class ProductPageLocators():
    ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    MESSAGE_ABOUT_ADDING = (By.CSS_SELECTOR, "div.alertinner")  # The shellcoder's handbook был добавлен в вашу корзину.
    PRODUCT_NAME = (By.CSS_SELECTOR, "div.product_main h1")  # название книжки
    MESSAGE_BASKET_TOTAL = (By.CSS_SELECTOR, ".alert-info .alertinner strong")  # общая цена товаров в корзине
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")  # цена самого товара за штуку

