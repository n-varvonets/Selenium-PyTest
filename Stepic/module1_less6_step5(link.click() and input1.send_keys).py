import math
from selenium import webdriver
import time

link = "http://suninjuly.github.io/find_link_text"
value = str(math.ceil(math.pow(math.pi, math.e)*10000))
value1 = 'input'
value2 = "last_name"
value3 = 'city'
value4 = 'country'


with webdriver.Chrome(executable_path='C:/Users/nicko/Downloads/chromedriver_win32/chromedriver.exe') as browser:
    browser.get(link)
    link = browser.find_element_by_link_text(value)
    link.click()
    input1 = browser.find_element_by_tag_name(value1)
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_name(value2)
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_class_name(value3)
    input3.send_keys("Smolensk")
    input4 = browser.find_element_by_id(value4)
    input4.send_keys("Russia")
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
    time.sleep(30)






