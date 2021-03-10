from selenium import webdriver
import pytest

class TestAbs():

    link_1 = "http://suninjuly.github.io/registration1.html"
    link_2 = "http://suninjuly.github.io/registration2.html"
    first_name = '[placeholder="Input your first name"]'
    last_name = '[placeholder="Input your last name"]'
    email = '[placeholder="Input your email"]'
    browser = webdriver.Chrome(executable_path='C:/Users/NIk/PycharmProjects/chromedriver.exe')

    def test_link_1(self):  #
        self.browser.get(self.link_1)
        self.browser.implicitly_wait(5)
        self.browser.find_element_by_css_selector(self.first_name).send_keys("Ivan")
        self.browser.find_element_by_css_selector(self.last_name).send_keys("Petrov")
        self.browser.find_element_by_css_selector(self.email).send_keys("Odessa")
        self.browser.find_element_by_css_selector("button.btn").click()
        welcome_text_elt = self.browser.find_element_by_tag_name("h1")
        welcome_text = welcome_text_elt.text
        assert "Congratulations! You have successfully registered!" == welcome_text

    def test_link_2(self):
        self.browser.get(self.link_2)
        self.browser.implicitly_wait(5)
        self.browser.find_element_by_css_selector(self.first_name).send_keys("Ivan")
        self.browser.find_element_by_css_selector(self.last_name).send_keys("Petrov")
        self.browser.find_element_by_css_selector(self.email).send_keys("Odessa")
        self.browser.find_element_by_css_selector("button.btn").click()
        welcome_text_elt = self.browser.find_element_by_tag_name("h1")
        welcome_text = welcome_text_elt.text
        assert "Congratulations! You have successfully registered!" == welcome_text


if __name__ == "__main__":
    pytest.main()





