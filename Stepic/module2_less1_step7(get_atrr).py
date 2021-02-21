from selenium import webdriver
import time
import math

link = "http://suninjuly.github.io/get_attribute.html"

id_answear = 'answer'
id_checkbox = "[id='robotCheckbox']"
radiobutton_id = "[id='robotsRule']"


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


with webdriver.Chrome(executable_path='C:/Users/nicko/Downloads/chromedriver_win32/chromedriver.exe') as browser:
    try:
        browser.get(link)

        treasure_id = browser.find_element_by_id("treasure")
        x_element = treasure_id.get_attribute("valuex")
        result_calc = str(calc(x_element))
        browser.find_element_by_id(id_answear).send_keys(result_calc)

        checkobox_robot = browser.find_element_by_css_selector(id_checkbox).click()
        radiobutton_robot = browser.find_element_by_css_selector(radiobutton_id).click()

        button = browser.find_element_by_css_selector("[type='submit']").click()



    except Exception as e:
        print(e)
    time.sleep(10)
    browser.quit()
