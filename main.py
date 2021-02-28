from selenium import webdriver
import unittest
from selenium.webdriver.common.keys import Keys
import time
import sys




class LoginIWannaBe(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path='C:/Users/nicko/Downloads/chromedriver_win32/chromedriver.exe')
        self.driver.get('https://iwannabe.web-magic.space/')

    def test_01(self):
        driver = self.driver
        try:
            assert "Python" in driver.title
        except Exception:
            print('Err in LoginIWannaBe by test_01')
            print(sys.exc_info())

    def test_02(self):
        driver = self.driver
        button_login = driver.find_element_by_link_text('/login')
        button_login.send_keys(Keys.ENTER)

        time.sleep(2)

        try:
            assert "Python" in driver.title
        except Exception:
            print('Err in LoginIWannaBe by test_02')
            print(sys.exc_info())

        asddsad  = driver.find_element_by_class_name("login-img")

        assert "Python" in driver.title
        elem = driver.find_element_by_name("q")
        elem.send_keys("pycon")
        elem.send_keys(Keys.RETURN)
        assert "No results found." not in driver.page_source
        driver.close()

#         '''1st successful try: https://habr.com/ru/post/250921/  ''''
#         driver = webdriver.Chrome(executable_path='C:/Users/nicko/Downloads/chromedriver_win32/chromedriver.exe')
#         driver.get("http://www.python.org")
#         assert "Python" in driver.title
#         elem = driver.find_element_by_name("q")
#         elem.send_keys("pycon")
#         elem.send_keys(Keys.RETURN)
#         assert "No results found." not in driver.page_source
#         driver.close()

    """2st successful try:Python + Selenium WebDriver - Видео №5"""
    def test_2stTry (self):
        driver = self.driver

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()


