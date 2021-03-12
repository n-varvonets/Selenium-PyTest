from .base_page import BasePage
from selenium.webdriver.common.by import By

class MainPage(BasePage):

    # def go_to_login_page(browser):
    """Чтобы все работало, надо слегка видоизменить его. В аргументы больше не надо передавать экземпляр браузера,
     мы его передаем и сохраняем на этапе создания Page Object. Вместо него нужно указать аргумент self,
        чтобы иметь доступ к атрибутам и методам класс"""

    def go_to_login_page(self):
        # login_link = self.browser.find_element_by_css_selector("#login_link")
        login_link = self.browser.find_element(By.CSS_SELECTOR, "#login_link")
        login_link.click()

    """в классе MainPage нужно реализовать метод, который будет проверять наличие ссылки(login)"""
    def should_be_login_link(self):
        # self.browser.find_element(By.CSS_SELECTOR, "#login_link_invalid")  # первончальный способ(до создани в
        # BasePage метода проверки присутствия элемента на странице is_element_present)
        assert self.is_element_present(By.CSS_SELECTOR, "#login_link"), "Login link is not presented"  # используем
        # созданный метод и добавляем возможнсоть осмысленного сообщение об ошибке
