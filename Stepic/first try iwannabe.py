from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

xpath_sign_up = '//a[text()="Sign up"]'
link_main_page = 'https://iwannabe.web-magic.space/'
id_first_name = 'first_name'
id_last_name = 'last_name'
id_email = 'email'
id_pass = 'password'
id_confirm_pass = 'password_confirmation'
button_type = "[type='submit']"
xpath_menu = "div[class='menu-mob-ic']"

id_phone = "phone"
id_birthday = "birthday"
id_address_1 = "address_1"
id_city = "city"
id_postcode = "postcode"
find_select_back_of_date = 'svg[version="1.1"][x="0px"][y="0px"]'
xpath_date_birthday = '//span[text()="5"]'
block_of_birthday = 'owl-dt-calendar-main'

with webdriver.Chrome(executable_path='C:/Users/NIk/PycharmProjects/chromedriver.exe') as browser:
    try:
        browser.get(link_main_page)
        browser.implicitly_wait(5)

        if browser.find_element_by_css_selector(xpath_menu):  # browser.maximize_window()
            browser.find_element_by_css_selector(xpath_menu).click()
        click_on_sign_up = browser.find_element_by_xpath(xpath_sign_up).click()

        input_first_name = browser.find_element_by_id(id_first_name).send_keys("Ivan")
        input_last_name = browser.find_element_by_id(id_last_name).send_keys("Ivanov")
        input_email = browser.find_element_by_id(id_email).send_keys("UA@gmail.com")
        input_pass = browser.find_element_by_id(id_pass).send_keys("QQQqqq111")
        input_confirm_pass = browser.find_element_by_id(id_confirm_pass).send_keys("QQQqqq111")
        confirm_first_page = browser.find_element_by_css_selector(button_type).click()
        input_phone = browser.find_element_by_id(id_phone).send_keys("06399999999")

        select_at_form_birthday = browser.find_element_by_id(id_birthday).click()
        # select_back = browser.find_element_by_css_selector(find_select_back_of_date).click()
        # select_date_birthday = browser.find_element_by_xpath(xpath_date_birthday).click()

        browser.execute_script("arguments[0].value = arguments[1]", select_at_form_birthday, '12/12/2017')

        input_city = browser.find_element_by_id(id_city).send_keys("Odessa")
        input_postcode = browser.find_element_by_id(id_postcode).send_keys("777")

        confirm_second_page = browser.find_element_by_css_selector(button_type).click()

    except Exception as e:
        print(e)
    time.sleep(210)
    browser.quit()


