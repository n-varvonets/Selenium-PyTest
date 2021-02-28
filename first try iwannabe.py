from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
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

text_for_criminal_field = '"Do you have any criminal offences or any pending legal action? ' \
                          'Do you have any criminal offences or any pending legal action?"'

with webdriver.Chrome(executable_path='C:/Users/NIk/PycharmProjects/chromedriver.exe') as browser:
    try:
        browser.maximize_window()
        browser.get(link_main_page)
        browser.implicitly_wait(5)
        click_on_sign_up = browser.find_element_by_xpath(xpath_sign_up).click()

        input_first_name = browser.find_element_by_id(id_first_name).send_keys("Ivan")
        input_last_name = browser.find_element_by_id(id_last_name).send_keys("Ivanov")
        input_email = browser.find_element_by_id(id_email).send_keys("qqqU__A@gmail.com")
        input_pass = browser.find_element_by_id(id_pass).send_keys("QQQqqq111")
        input_confirm_pass = browser.find_element_by_id(id_confirm_pass).send_keys("QQQqqq111")
        confirm_first_page = browser.find_element_by_css_selector(button_type).click()

        input_phone = browser.find_element_by_id(id_phone).send_keys("06399999999")
        select_at_form_birthday = browser.find_element_by_id(id_birthday).click()
        select_back = browser.find_element_by_css_selector(find_select_back_of_date).click()
        select_date_birthday = browser.find_element_by_xpath(xpath_date_birthday).click()
        input_address = browser.find_element_by_id("address_1").send_keys("Odessa str")
        input_city = browser.find_element_by_id(id_city).send_keys("Odessa")
        input_postcode = browser.find_element_by_id(id_postcode).send_keys("777")
        confirm_second_page = browser.find_element_by_class_name("__step-2")
        actions = ActionChains(browser)
        actions.move_to_element(confirm_second_page).send_keys(Keys.ENTER).perform()

        current_place_of_education = browser.find_element_by_css_selector("[placeholder='Current place of education']").send_keys("IFNTUOG")
        contact_number = browser.find_element_by_css_selector('[placeholder="Contact phone"]').send_keys("063666666666")
        name_of_careers_advisor = browser.find_element_by_css_selector('[placeholder="Full name of career’s contact at college"]').send_keys("name_of_careers_advisor")
        email_address = browser.find_element_by_css_selector('[placeholder="Their email address"]').send_keys("mail@mail.com")
        radio_1 = browser.find_element_by_css_selector('[for ="radio-1"]').click()
        radio_3 = browser.find_element_by_css_selector('[for ="radio-3"]').click()
        confirm_third_page = browser.find_element_by_css_selector(button_type).click()

        select_from_checkbox = browser.find_element_by_xpath("//div[@class ='ng-input']").click()
        select_checkbox = browser.find_element_by_css_selector('[class="ng-option ng-star-inserted"]').click()
        tick_the_statement = browser.find_element_by_css_selector('[for="disability-1"]').click()
        choose_your_ethnicity = browser.find_element_by_css_selector('[for="ethnicity-1"]').click()
        any_criminal = browser.find_element_by_css_selector('[for="radio-5"]').click()
        fill_criminal_field = browser.find_element_by_css_selector('[placeholder="Details criminal offense"]').send_keys(text_for_criminal_field)
        confirm_fourth_page = browser.find_element_by_css_selector(button_type).click()

    except Exception as e:
        print(e)
    time.sleep(2210)
    browser.quit()


