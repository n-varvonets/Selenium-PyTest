from selenium import webdriver
import time
import os

first_name = "[placeholder='Enter first name']"
last_name = "[placeholder='Enter last name']"
email = "[placeholder='Enter email']"
link = 'http://suninjuly.github.io/file_input.html'

with webdriver.Chrome(executable_path='C:/Users/NIk/PycharmProjects/chromedriver.exe') as browser:
    try:
        browser.get(link)
        input_first_name = browser.find_element_by_css_selector(first_name).send_keys("Ivan")
        input_last_name = browser.find_element_by_css_selector(last_name).send_keys("Petrov")
        input_email = browser.find_element_by_css_selector(email).send_keys("Smolensk")

        current_dir = os.path.abspath(os.path.dirname(__file__))
        file_name = "file_txt for mod2_less2_step8.txt"
        file_path = os.path.join(current_dir, file_name)
        element = browser.find_element_by_id('file')
        element.send_keys(file_path)

        button = browser.find_element_by_css_selector("[type='submit']").click()

    except Exception as e:
        print(e)
    time.sleep(110)
    browser.quit()

