from selenium import webdriver
import time
from selenium import webdriver
import math

link = "https://SunInJuly.github.io/execute_script.html"
id_x = 'input_value'
id_answear = 'answer'
id_robot = 'robotCheckbox'
for_checkobox = "[for='robotCheckbox']"


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


with webdriver.Chrome(executable_path='C:/Users/nicko/Downloads/chromedriver_win32/chromedriver.exe') as browser:
    try:
        browser.get(link)
        x_element = browser.find_element_by_id(id_x).text
        result_calc = str(calc(x_element))
        browser.find_element_by_id(id_answear).send_keys(result_calc)
        checkobox_robot = browser.find_element_by_id(id_robot).click()
        browser.execute_script("window.scrollBy(0, 100);")
        radiobutton_robot = browser.find_element_by_css_selector(for_checkobox).click()

    except Exception as e:
        print(e)
    time.sleep(110)
    browser.quit()




