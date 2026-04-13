# Напишіть цикл, який буде вимагати від користувача ввести слово, в якому є літера "h"
# (враховуються як великі так і маленькі). Цикл не повинен завершитися, якщо користувач ввів слово без букви "h".

while True:
    user_text = input('Please enter word with letter "h":')
    if "h" in user_text.lower():
        break
    else:
        continue
