import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_guest_should_see_login_link_pass(browser):
    browser.get(link)
    # time.sleep(10)  # для удобства визуальной проверки фразы кнопки "Ajouter au panier".
    assert browser.find_element_by_class_name("btn-add-to-basket")


""" Варианты запуска тестов: """
# pytest -s -v --language=es test_items.py - обычный запуск на испанском
# pytest -s -v --language=fr test_items.py - проверочный запуск на русском
# pytest -s -v --browser_name=firefox --language=fr test_items.py - браузер firefox на французком
