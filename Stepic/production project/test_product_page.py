from pages.product_page import AddTobasket
import time


def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = AddTobasket(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()                      # открываем страницу
    page.add_to_basket()             # выполняем метод страницы — переходим на страницу логина
    page.solve_quiz_and_get_code()
    page.check_methods_after_add_prod_to_cart()
    # time.sleep(995)




