from pages.main_page import MainPage
from pages.login_page import LoginPage

"""первый вид текста"""
# def test_guest_can_go_to_login_page(browser):
#     link = "http://selenium1py.pythonanywhere.com/"
#     browser.get(link)
#     login_link = browser.find_element_by_css_selector("#login_link")
#     login_link.click()

# pytest -v --tb=line --language=en test_main_page.py - для запуска
# --tb=line, которая указывает, что нужно выводить только одну строку из лога каждого упавшего теста.
# Так вам будет проще разобраться в том, как выглядят сообщения об ошибках.
# -v нужен для запуска набора тестов(но это не точно)

"""преобразуем второй вид текста"""
def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()                      # открываем страницу

    # page.go_to_login_page()          # выполняем метод страницы — переходим на страницу логина
    # page.should_be_login_link()      # добавили проверку на присутсвие эелемента на странице
    # reg_page = LoginPage(browser, link)
    # reg_page.should_be_login_page()

    login_page = page.go_to_login_page()
    login_page.should_be_login_page()

    """Плюсы такого подхода: 

тест выглядит аккуратнее — не нужно инициализировать страницу в теле теста;
явно возвращаем страницу — тип страницы ассоциирован с методом;
не нужно каждый раз думать в разных тестах про инициализацию страницы — уменьшаем дублирование кода;
минусы: 

если у нас копится большое количество страниц и переходов — образуется много перекрестных импортов;
большая связность кода — при изменении логики придется менять возвращаемое значение;
сложнее понимать код, так как страница инициализируется неявно;
образуются циклические зависимости, что часто приводит к ошибкам."""

