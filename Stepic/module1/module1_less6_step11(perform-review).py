from selenium import webdriver
import time

link_1 = "http://suninjuly.github.io/registration1.html"
link_2 = "http://suninjuly.github.io/registration1.html"
first_name = '[placeholder="Input your first name"]'
last_name = '[placeholder="Input your last name"]'
email = '[placeholder="Input your email"]'

with webdriver.Chrome(executable_path='C:/Users/nicko/Downloads/chromedriver_win32/chromedriver.exe') as browser:
    try:
        browser.get(link_1)
        browser.find_element_by_css_selector(first_name).send_keys("Ivan")
        browser.find_element_by_css_selector(last_name).send_keys("Petrov")
        browser.find_element_by_css_selector(email).send_keys("Odessa")
        button = browser.find_element_by_css_selector("button.btn")
        button.click()
        time.sleep(1)
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        welcome_text = welcome_text_elt.text
        assert "Congratulations! You have successfully registered!" == welcome_text

    except Exception as e:
        print(e)
    time.sleep(910)
    browser.quit()