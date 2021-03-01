def shout(word="да"):
    return word.capitalize() + "!"

print(shout()) # выведет: 'Да!'

# Так как функция - это объект, вы связать её с переменнной,
# как и любой другой объект
scream = shout

# Заметьте, что мы не используем скобок: мы НЕ вызываем функцию "shout",
# мы связываем её с переменной "scream". Это означает, что теперь мы
# можем вызывать "shout" через "scream":

print(scream())  # выведет: 'Да!'

# Более того, это значит, что мы можем удалить "shout", и функция всё ещё
# будет доступна через переменную "scream"

del shout
try:
    print(shout())
except NameError as e:
    print(e)

print(scream())
