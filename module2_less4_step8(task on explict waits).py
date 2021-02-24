from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

link = "http://suninjuly.github.io/explicit_wait2.html"

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


with webdriver.Chrome(executable_path='C:/Users/NIk/PycharmProjects/chromedriver.exe') as browser:
    try:
        browser.get(link)

        WebDriverWait(browser, 12).until(
                EC.text_to_be_present_in_element((By.ID, "price"), "100")
            )
        button_book = browser.find_element_by_id("book").click()

        x_element = browser.find_element_by_id("input_value").text
        result_calc = str(calc(x_element))

        input_in_form = browser.find_element_by_id('answer').send_keys(result_calc)

        button = browser.find_element_by_css_selector("[type='submit']").click()

    except Exception as e:
        print(e)
    time.sleep(15)
    browser.quit()