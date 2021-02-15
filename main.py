from selenium import webdriver
import unittest
from selenium.webdriver.common.keys import Keys
import time


class LoginIWannaBe(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://iwannabe.web-magic.space/')

    def test_01(self):
        driver = self.driver
        button_login = driver.driver.find_element_by_link_text('/login')
        button_login.send_keys(Keys.ENTER)

        time.sleep(2)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()


