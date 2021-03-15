from .base_page import BasePage
from .locators import MainPageLocators
from selenium.webdriver.common.by import By
from .login_page import LoginPage

"""Переход можно реализовать двумя разными способами. 
Первый способ: возвращать нужный Page Object."""

class MainPage(BasePage):

    # def go_to_login_page(browser):
    """Чтобы все работало, надо слегка видоизменить его. В аргументы больше не надо передавать экземпляр браузера,
     мы его передаем и сохраняем на этапе создания Page Object. Вместо него нужно указать аргумент self,
        чтобы иметь доступ к атрибутам и методам класс"""

    def go_to_login_page(self):
        # login_link = self.browser.find_element_by_css_selector("#login_link")  №1
        # login_link = self.browser.find_element(By.CSS_SELECTOR, "#login_link") №2
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)  # №3
        login_link.click()

        """Затем в методе, который осуществляет переход к странице логина,
               проинициализировать новый объект Page и вернуть его"""
        return LoginPage(browser=self.browser, url=self.browser.current_url)  # При создании объекта мы обязательно
        # передаем ему тот же самый объект драйвера для работы с браузером, а в качестве url передаем текущий адрес


    """в классе MainPage нужно реализовать метод, который будет проверять наличие ссылки(login)"""
    def should_be_login_link(self):
        # self.browser.find_element(By.CSS_SELECTOR, "#login_link")  # №1 первончальный способ(до создани в
        # BasePage метода проверки присутствия элемента на странице is_element_present)

        # assert self.is_element_present(By.CSS_SELECTOR, "#login_link"), "Login link is not presented" # №2 второй вариант
        # используем созданный метод и добавляем возможнсоть осмысленного сообщение об ошибке (но без использования локаторов)

        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"  # символ *, он
        # указывает на то, что мы передали именно пару, и этот кортеж нужно распаковать.

