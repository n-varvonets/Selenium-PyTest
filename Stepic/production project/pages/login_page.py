from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        current_url = self.browser.current_url
        # print(current_url)  # http://selenium1py.pythonanywhere.com/en-gb/accounts/login/
        assert current_url in "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/", "Login url is not presented"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.USER_LOGIN_NAME), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.USER_REG_NAME), "Register form is not presented"

    def register_new_user(self, email, password):
        self.browser.find_element(*LoginPageLocators.USER_REG_NAME).send_keys(email)
        self.browser.find_element(*LoginPageLocators.USER_LOGIN_PASS_1).send_keys(password)
        self.browser.find_element(*LoginPageLocators.USER_LOGIN_PASS_2).send_keys(password)
        self.browser.find_element(*LoginPageLocators.BTN_REG_SUBMIT).click()


