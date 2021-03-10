from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class TestButton:
    def test_guest_should_see_adding_to_card(self, browser):
        link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        browser.get(link)
        button = WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR,
                                                                                    ".btn.btn-lg.btn-primary")))
        assert button.is_displayed, f"{button} is not showing on the page"
