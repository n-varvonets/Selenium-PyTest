from selenium import webdriver
import time
import math

submit = "[type='submit']"
link = 'http://suninjuly.github.io/alert_accept.html'


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


with webdriver.Chrome(executable_path='C:/Users/NIk/PycharmProjects/chromedriver.exe') as browser:
    try:
        browser.get(link)
        input_confirm_butt = browser.find_element_by_css_selector(submit).click()
        alert = browser.switch_to.alert
        alert.accept()

        x_element = browser.find_element_by_id("input_value").text
        result_calc = str(calc(x_element))

        input_in_form = browser.find_element_by_id('answer').send_keys(result_calc)

        button = browser.find_element_by_css_selector("[type='submit']").click()

    except Exception as e:
        print(e)
    time.sleep(10)
    browser.quit()

