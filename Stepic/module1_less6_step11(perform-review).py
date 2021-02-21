from selenium import webdriver
import time

link = "http://suninjuly.github.io/registration2.html"
sel1 = '.first_block .form-control.first'
sel2 = '.first_block .form-control.second'
sel3 = '.first_block .form-control.third'

with webdriver.Chrome() as browser:
    try:
        browser.get(link)
        browser.find_element_by_css_selector(sel1).send_keys("Ivan")
        browser.find_element_by_css_selector(sel2).send_keys("Petrov")
        browser.find_element_by_css_selector(sel3).send_keys("Odessa")
        button = browser.find_element_by_css_selector("button.btn")
        button.click()
        time.sleep(1)
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        welcome_text = welcome_text_elt.text
        assert "Congratulations! You have successfully registered!" == welcome_text

    except Exception as e:
        print(e)
    time.sleep(10)
    browser.quit()


"""my first try, when I find all required(not-unique) elements"""
# value_by_xpath = '//div[@class="first_block"]//input[@type="text"]'
# value_by_class = '.first_block input.form-control'  # 2nd way
# link = "http://suninjuly.github.io/registration1.html"
#
# try:
#     browser = webdriver.Chrome()
#     browser.get(link)
#     elements = browser.find_elements_by_css_selector(value_by_class)
#     # elements = browser.find_elements_by_css_selector(value_by_class)  # 2nd way
#     for element in elements:
#         element.send_keys("Мой ответ")
#     button = browser.find_element_by_css_selector("button.btn")
#     time.sleep(3)
#     button.click()
#     time.sleep(3)
#     welcome_text_elt = browser.find_element_by_tag_name("h1")
#     welcome_text = welcome_text_elt.text
#     assert "Congratulations! You have successfully registered!" == welcome_text
#
# finally:
#     time.sleep(3)
#     browser.quit()
