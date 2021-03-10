"""2(1)/13"""
# from selenium import webdriver
#
# browser = webdriver.Chrome(executable_path='C:/Users/nicko/Downloads/chromedriver_win32/chromedriver.exe')
# browser.get("http://suninjuly.github.io/simple_form_find_task.html")
# button = browser.find_element_by_id("submit_button")

"""2(2)/13"""
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome(executable_path='C:/Users/nicko/Downloads/chromedriver_win32/chromedriver.exe')
browser.get("http://suninjuly.github.io/simple_form_find_task.html")
button = browser.find_element(By.ID, "submit_button")



