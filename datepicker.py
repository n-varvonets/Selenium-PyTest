from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://seleniumpractise.blogspot.com/2016/08/how-to-handle-calendar-in-selenium.html"

driver = webdriver.Chrome(executable_path='C:/Users/NIk/PycharmProjects/chromedriver.exe')
driver.maximize_window()
driver.get(link)
driver.implicitly_wait(5)
driver.find_element(By.ID, "datepicker").click()
# driver.find_element(By.XPATH, "//a[text()='24']").click()
all_dates = driver.find_elements(By.XPATH, "//table[@class='ui-datepicker-calendar']//a")

for date_el in all_dates:
    date = date_el.text
    if date == "23":
        date_el.click()