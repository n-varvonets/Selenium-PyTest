from selenium import webdriver
import time
import math

link = "http://suninjuly.github.io/math.html"
id_x = 'input_value'
id_answear = 'answer'
for_checkbox = "[for='robotCheckbox']"
radiobutton_for = "[for='robotsRule']"


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


with webdriver.Chrome(executable_path='C:/Users/nicko/Downloads/chromedriver_win32/chromedriver.exe') as browser:
    try:
        browser.get(link)

        x_element = browser.find_element_by_id(id_x).text
        result_calc = str(calc(x_element))
        browser.find_element_by_id(id_answear).send_keys(result_calc)

        checkobox_robot = browser.find_element_by_css_selector(for_checkbox).click()
        radiobutton_robot = browser.find_element_by_css_selector(radiobutton_for).click()

        button = browser.find_element_by_css_selector("button.btn")
        button.click()



    except Exception as e:
        print(e)
    time.sleep(10)
    browser.quit()
