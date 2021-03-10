from selenium import webdriver
import time
import math

link = "http://suninjuly.github.io/selects1.html"

id_num1 = 'num1'
id_num2 = 'num2'
# id_checkbox = "[id='robotCheckbox']"
# radiobutton_id = "[id='robotsRule']"


with webdriver.Chrome(executable_path='C:/Users/nicko/Downloads/chromedriver_win32/chromedriver.exe') as browser:
    try:
        browser.get(link)

        num1 = browser.find_element_by_id(id_num1).text
        num2 = browser.find_element_by_id(id_num2).text
        result_of_sum = int(num1) + int(num2)

        browser.find_element_by_css_selector(f"[value='{result_of_sum}']").click()
        button = browser.find_element_by_css_selector("[type='submit']").click()

    except Exception as e:
        print(e)
    time.sleep(10)
    browser.quit()


"""EXAMPLE"""
# <label for="dropdown">Выберите язык программирования:</label>
# <select id="dropdown" class="custom-select">
# <option selected>--</option>
# <option value="1">Python</option>
# <option value="2">Java</option>
# <option value="3">JavaScript</option>
# </select>

# from selenium import webdriver
# from selenium.webdriver.support.ui import Select
#
# browser = webdriver.Chrome()
# browser.get(link)

"""first basic way by clicking on button of list"""
# browser.find_element_by_tag_name("select").click()
# browser.find_element_by_css_selector("option:nth-child(2)").click()
# browser.find_element_by_css_selector("[value='1']").click()  # 2nd way to click

"""2nd way by clicking on button of list"""
# select = Select(browser.find_element_by_tag_name("select"))  # select.select_by_visible_text("Python") select.select_by_index(0)
# select.select_by_value("1")  # ищем элемент с текстом "Python"

