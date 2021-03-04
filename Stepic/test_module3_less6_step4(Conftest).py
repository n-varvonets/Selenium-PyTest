import pytest
from selenium import webdriver
import math
import time

def calc(x):
  return str(math.log(int(time.time() - 21.3)))


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome(executable_path='C:/Users/NIk/PycharmProjects/chromedriver.exe')
    yield browser
    print("\nquit browser..")
    browser.quit()

@pytest.mark.parametrize('links', ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"])
def test_guest_should_see_login_link(browser, links):
    link = f"https://stepik.org/lesson/{links}/step/1/"
    browser.get(link)
    browser.implicitly_wait(5)
    res = str(calc(time.time()))
    browser.find_element_by_xpath("//textarea").send_keys(res)
    browser.find_element_by_class_name("submit-submission").click()
    correct = browser.find_element_by_class_name("smart-hints__hint").text
    assert "Correct!" == correct

# pytest -s -v test_module3_less6_step3.py

