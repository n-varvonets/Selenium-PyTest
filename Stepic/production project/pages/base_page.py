from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException # в начале файла
import math
import time

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


