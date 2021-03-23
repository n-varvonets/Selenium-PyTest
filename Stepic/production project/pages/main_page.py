from .base_page import BasePage


class MainPage(BasePage): 
    """т.к. def go_to_login_page и def should_be_login_link мы перенесли в base_page для DRY, то ставим заглушку"""
    def __init__(self, *args, **kwargs):  # метод __init__ вызывается при создании объекта
        super(MainPage, self).__init__(*args, **kwargs)  # super на самом деле только вызывает конструктор класса предка
        # и передает ему все те аргументы, которые мы передали в конструктор MainPage.

