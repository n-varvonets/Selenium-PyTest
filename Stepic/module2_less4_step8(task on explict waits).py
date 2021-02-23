from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time

link = "http://suninjuly.github.io/explicit_wait2.html"

with webdriver.Chrome(executable_path='C:/Users/NIk/PycharmProjects/chromedriver.exe') as browser:
    try:
        browser.get(link)

        button = WebDriverWait(browser, 12).until(
                EC.element_to_be_clickable((By.ID, "book"))
            )
        button.click()
        # message = browser.find_element_by_id("verify_message")
        #
        # assert "successful" in message.text

    except Exception as e:
        print(e)
    time.sleep(15)
    browser.quit()