"""Alert является модальным окном: это означает, что пользователь
не может взаимодействовать дальше с интерфейсом, пока не закроет alert."""

# 1й window - accept():
alert = browser.switch_to.alert  # ереключиться на окно с alert
alert_text = alert.text  # получить текст из alert
alert.accept()

# 2ое window - confirm
confirm = browser.switch_to.alert
confirm.accept()
confirm.dismiss()  # или можно отменить

# 3 window -  prompt — имеет дополнительное поле для ввода текста. Чтобы ввести текст, используйте метод send_keys():
prompt = browser.switch_to.alert
prompt.send_keys("My answer")
prompt.accept()