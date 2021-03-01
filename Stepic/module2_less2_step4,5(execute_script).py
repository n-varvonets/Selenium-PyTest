from selenium import webdriver
import time
from selenium import webdriver

link = "https://SunInJuly.github.io/execute_script.html"

with webdriver.Chrome(executable_path='C:/Users/nicko/Downloads/chromedriver_win32/chromedriver.exe') as browser:
    try:
        browser.get(link)
        """example executing code with changed title and submit btn"""
        # browser.execute_script("document.title='Script executing';alert('Robots at work');")

        """Эта команда проскроллит страницу на 100 пикселей вниз:"""
        # browser.execute_script("window.scrollBy(0, 100);")

        """Как вариант еще можно скрывать ненужный элемент"""
        # browser.execute_script('arguments[0].style.visibility = \'hidden\'', footer)

        """Еще в глобальном смысле мотнуть в самый верх или самый низ страницы можно и питоном для тега body"""
        # from selenium.webdriver.common.keys import Keys
        # browser.find_element_by_tag_name('body').send_keys(Keys.END)  # или Home если наверх

        """If you face with next err:'Message: element click intercepted:..'(Если элемент оказывается перекрыт
         другим элементом...чтобы кликнуть на перекрытую кнопку, нам нужно выполнить следующие команды в коде"""
        # button = browser.find_element_by_tag_name("button").click()
        # assert True

        """Для сравнения приведем скрипт на этом языке, который делает то же, что 
               приведенный пример для WebDriver://javascript"""
        # button = document.getElementsByTagName("button")[0];
        # button.scrollIntoView(true);
        # button = browser.find_element_by_css_selector("[type='submit']").click()

        """А сейчас в коде от только что приведенного выше примера который вбивается в консоль для быстрого поиска"""
        button = browser.find_element_by_tag_name("button")
        browser.execute_script("return arguments[0].scrollIntoView(true);", button).click()  # true, чтобы элемент после
        # скролла оказался в области видимости.

    except Exception as e:
        print(e)
    time.sleep(30)
    browser.quit()




