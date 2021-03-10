"""
- Кнопка может быть неактивной, то есть её нельзя кликнуть;
- Кнопка может содержать текст, который меняется в зависимости от действий пользователя. Например, текст "Отправить"
после нажатия кнопки поменяется на "Отправлено";
- Кнопка может быть перекрыта каким-то другим элементом или быть невидимой.
"""

"""1ый вариант с ошибкой - Если мы хотим в тесте кликнуть на кнопку, а она в этот момент неактивна"""
# from selenium import webdriver
#
# browser = webdriver.Chrome(executable_path='C:/Users/NIk/PycharmProjects/chromedriver.exe')
# # говорим WebDriver ждать все элементы в течение 5 секунд
# browser.implicitly_wait(5)
#
# browser.get("http://suninjuly.github.io/wait2.html")
#
# button = browser.find_element_by_id("verify")
# button.click()
# message = browser.find_element_by_id("verify_message")
#
# assert "successful" in message.text
# Мы видим, что WebDriver смог найти кнопку с id="verify" и кликнуть по ней, но тест упал на поиске элемента с итоговым
# сообщением: no such element: Unable to locate element: {"method":"id","selector":"verify_message"}
# ------------------------------------------------------------
"""2ой вариант решение - явных ожиданий(Explicit Waits)позволяют задать специальное ожидание для конкретного элемента"""

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

browser = webdriver.Chrome(executable_path='C:/Users/NIk/PycharmProjects/chromedriver.exe')

browser.get("http://suninjuly.github.io/wait2.html")

# говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
button = WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.ID, "verify"))
    )  # функция until передается правило ожидания, элемент, а также значение, по которому мы будем искать элемент
button.click()
message = browser.find_element_by_id("verify_message")

assert "successful" in message.text

"""В модуле expected_conditions есть много других правил, которые позволяют реализовать необходимые ожидания:

# .text_to_be_present_in_element((By.ID, "здесь пишем ID"), "здесь текст")

title_is
title_contains
presence_of_element_located
visibility_of_element_located
visibility_of
presence_of_all_elements_located
text_to_be_present_in_element
text_to_be_present_in_element_value
frame_to_be_available_and_switch_to_it
invisibility_of_element_located
element_to_be_clickable
staleness_of
element_to_be_selected
element_located_to_be_selected
element_selection_state_to_be
element_located_selection_state_to_be
alert_is_present

Описание каждого правила можно найти на сайте ниже
https://selenium-python.readthedocs.io/api.html#module-selenium.webdriver.support.expected_conditions"""

# говорим Selenium проверять в течение 5 секунд пока кнопка станет неактивной
# button = WebDriverWait(browser, 5).until_not(
#         EC.element_to_be_clickable((By.ID, "verify"))
#     )

