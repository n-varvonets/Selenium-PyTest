# Selenium-PyTest

For running project for review you need:

1)go to necessary directory with next cmd:
- **cd Stepic/production project**

2)execute cmd for running tests:
- **pytest -s -v --tb=line test_product_page.py**  - for all tests
- **pytest -v --tb=line --language=en -m need_review** -  for review marked tests

                      -------------------------------Stucure of module4-------------------------------
**base_page.py** - тут мы храним методы которые применяются по всему проекту вообще, всё завернуто в класс, чтобы было удобно импортировать.

**locators.py** - тут мы храним локаторы, в виде констант. Локаторы каждой отдельной страницы завёрнуты в класс, чтобы было удобно импортировать

**main_page.py** - тут мы храним методы по конкретной странице, завернутые в класс этой странице. Класс этот - условный MainPage - наследник класса BasePage, чтобы можно было пользоваться методами, описанными в base_page.py

**test_main_page.py** - тут мы будем хранить сами тест-кейсы, которые будем запускать с помощью pytest. Тут вызванные функции будут запускаться:
- выдаём нужный для проверки линк
- создаём в функции переменную page, которой передаём браузер из base_page.py(класс BasePage) и линк из шага №1
- следом говорим "page, откройся", но методом из base_page.py(класс BasePage)
- добавляем проверки, которые создавали методами в main_page.py
