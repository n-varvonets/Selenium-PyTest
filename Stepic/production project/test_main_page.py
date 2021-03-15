from pages.main_page import MainPage
from pages.login_page import LoginPage


def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = MainPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()                      # открываем страницу

    page.go_to_login_page()          # выполняем метод страницы — переходим на страницу логина
    page.should_be_login_link()      # добавили проверку на присутсвие эелемента на странице

    # reg_page = LoginPage(browser, link)
    # reg_page.should_be_login_page()

    login_page = page.go_to_login_page()
    login_page.should_be_login_page()

# pytest -s -v --tb=line --language=en test_main_page.py - для запуска



