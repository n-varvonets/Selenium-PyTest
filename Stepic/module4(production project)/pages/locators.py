"""орошей практикой является выносить селектор во внешнюю переменную"""

from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")  # теперь каждый селектор — это пара: как искать и что искать.


class LoginPageLocators():
    LOGIN_URL = (By.CSS_SELECTOR, "#login_url")
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FROM = (By.CSS_SELECTOR, "#register_form")

