from selenium import webdriver
import time

value_by_xpath = '//div[@class="first_block"]//input[@type="text"]'
value_by_class = '.first_block input.form-control'
link = "http://suninjuly.github.io/registration1.html"

try:
    browser = webdriver.Chrome(executable_path='C:/Users/nicko/Downloads/chromedriver_win32/chromedriver.exe')
    browser.get(link)
    elements = browser.find_elements_by_css_selector(value_by_class)
    for element in elements:
        element.send_keys("Мой ответ")
    button = browser.find_element_by_css_selector("button.btn")
    time.sleep(3)
    button.click()
    time.sleep(3)
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    welcome_text = welcome_text_elt.text
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(3)
    browser.quit()
