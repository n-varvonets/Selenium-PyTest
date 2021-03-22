from telnetlib import EC

from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.common.exceptions import NoAlertPresentException # в начале файла
import math
import time

from selenium.webdriver.support.wait import WebDriverWait


class BasePage():

    def __init__(self, browser, url, timeout=15):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert  # переключаемся на alert
        x = alert.text.split(" ")[2]  # берем "х" - второй эелемент текстовго представления из alert
        answer = str(math.log(abs((12 * math.sin(float(x))))))  # подставляем х в выражение и получаем овтет
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert  # меняется alert и получаем наш ответ для степика
            alert_text = alert.text   # ответ переводим в текст
            print(f"Your code: {alert_text}")  # печатем тестовый ответ в консоль
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    """проверяет, что элемент не появляется на странице в течение заданного времени"""
    def is_not_element_present(self, how, what, timeout=4):  # упадет, как только увидит искомый элемент. Не появился: успех, тест зеленый.
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True
        return False

    """Если же мы хотим проверить, что какой-то элемент исчезает, то следует воспользоваться явным ожиданием """
    def is_disappeared(self, how, what, timeout=4):  # будет ждать до тех пор, пока элемент не исчезнет.
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException). \
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False

        return True


