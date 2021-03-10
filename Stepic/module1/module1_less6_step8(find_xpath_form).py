from selenium import webdriver
import time

link = "http://suninjuly.github.io/find_xpath_form"

value1 = 'input'
value2 = "last_name"
value3 = 'city'
value4 = 'country'
value5 = '//*[@type="submit"]'

with webdriver.Chrome(executable_path='C:/Users/nicko/Downloads/chromedriver_win32/chromedriver.exe') as browser:
    try:
        browser.get("http://suninjuly.github.io/find_xpath_form")
        browser.find_element_by_tag_name(value1).send_keys("Ivan")
        browser.find_element_by_name(value2).send_keys("Petrov")
        browser.find_element_by_class_name(value3).send_keys("Smolensk")
        browser.find_element_by_id(value4).send_keys("Russia")
        browser.find_element_by_xpath(value5).click()

    except Exception as e:
        print(e)
    time.sleep(10)
    browser.quit()

