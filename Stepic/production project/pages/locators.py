from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")


class BasketPageLocators():
    BASKET_LINK = (By.CSS_SELECTOR, "span a.btn.btn-default")
    BASKET_ITEMS = (By.CSS_SELECTOR, "basket-items")
    BASKET_SMS_EMPTY = (By.CSS_SELECTOR, "#content_inner")


class LoginPageLocators():
    USER_LOGIN_NAME = (By.CSS_SELECTOR, "#id_login-username")
    USER_LOGIN_EMAIL = (By.CSS_SELECTOR, "#id_login-password")
    USER_REG_NAME = (By.CSS_SELECTOR, "#id_registration-email")
    USER_LOGIN_PASS_1 = (By.CSS_SELECTOR, "#id_registration-password1")
    USER_LOGIN_PASS_2 = (By.CSS_SELECTOR, "#id_registration-password2")
    BTN_REG_SUBMIT = (By.CSS_SELECTOR, "[name='registration_submit']")

    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class ProductPageLocators():
    ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    MESSAGE_ABOUT_ADDING = (By.CSS_SELECTOR, "div.alertinner strong")  # The shellcoder's handbook был добавлен в вашу корзину.(ез стронг)
    PRODUCT_NAME = (By.CSS_SELECTOR, "div.product_main h1")  # название книжки
    MESSAGE_BASKET_TOTAL = (By.CSS_SELECTOR, ".alert-info .alertinner strong")  # общая цена товаров в корзине
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")  # цена самого товара за штуку
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-success")

