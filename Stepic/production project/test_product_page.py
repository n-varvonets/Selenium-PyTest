from pages.product_page import AddToBasket


def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = AddToBasket(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()                      # открываем страницу
    page.add_to_basket()             # выполняем метод страницы — переходим на страницу логина
    page.solve_quiz_and_get_code()
    page.check_methods_after_add_prod_to_cart()


