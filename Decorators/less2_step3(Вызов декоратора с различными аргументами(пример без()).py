def decorator_maker():
    print("Я создаю декораторы! Я буду вызван только раз: " + \
    "когда ты попросишь меня создать тебе декоратор.")

    def my_decorator(func):
        print("Я - декоратор! Я буду вызван только раз: в момент декорирования функции.")

        def wrapped():
            print("Я - обёртка вокруг декорируемой функции. "
                  "Я буду вызвана каждый раз когда ты вызываешь декорируемую функцию. "
                  "Я возвращаю результат работы декорируемой функции.")
            return func()

        print("Я возвращаю обёрнутую функцию.")
        return wrapped

    print("Я возвращаю декоратор.")
    return my_decorator


# Давайте теперь создадим декоратор. Это всего лишь ещё один вызов функции
new_decorator = decorator_maker()  # выведет:
# Я создаю декораторы! Я буду вызван только раз: когда ты попросишь меня создать тебе декоратор. 
# Я возвращаю декоратор.
print('--------------1.1-------------')

# Теперь декорируем функцию

def decorated_function():
    print("Я - декорируемая функция!@!@.")


decorated_function = new_decorator(decorated_function)  # выведет:
# Я - декоратор! Я буду вызван только раз: в момент декорирования функции.
# Я возвращаю обёрнутую функцию.
print('--------------1.2-------------')

# Теперь наконец вызовем функцию:
decorated_function()  # выведет:
# Я - обёртка вокруг декорируемой функции. Я буду вызвана каждый раз когда ты вызываешь декорируемую функцию.
# Я возвращаю результат работы декорируемой функции.
# Я - декорируемая функция.
print('--------------1.3-------------')

# -----------------------------------------------------------------------------------------------------------------
"""Длинно? Длинно. Перепишем данный код без использования промежуточных переменных:"""

def decorated_function():
    print("Я - декорируемая функция-----.")
decorated_function = decorator_maker()(decorated_function)  # выведет:
# Я создаю декораторы! Я буду вызван только раз: когда ты попросишь меня создать тебе декоратор.
# Я возвращаю декоратор.
# Я - декоратор! Я буду вызван только раз: в момент декорирования функции.
# Я возвращаю обёрнутую функцию.
print('--------------2.1-------------')

# Наконец:
decorated_function()  # выведет:
# Я - обёртка вокруг декорируемой функции. Я буду вызвана каждый раз когда ты вызываешь декорируемую функцию.
# Я возвращаю результат работы декорируемой функции.
# Я - декорируемая функция.
print('--------------2.2-------------')

# -----------------------------------------------------------------------------------------------------------------
"""А теперь ещё раз, ещё короче:"""
@decorator_maker()
def decorated_function():
    print("I am the decorated function.")  # выведет:
# Я создаю декораторы! Я буду вызван только раз: когда ты попросишь меня создать тебе декоратор.
# Я возвращаю декоратор.
# Я - декоратор! Я буду вызван только раз: в момент декорирования функции.
# Я возвращаю обёрнутую функцию.
print('--------------3.1-------------')

# И снова:
decorated_function()  # выведет:
# Я - обёртка вокруг декорируемой функции. Я буду вызвана каждый раз когда ты вызываешь декорируемую функцию.
# Я возвращаю результат работы декорируемой функции.
# Я - декорируемая функция.
print('--------------3.2-------------')

"""Вы заметили, что мы вызвали функцию, после знака "@"?:)"""


