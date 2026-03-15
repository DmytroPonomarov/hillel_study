# Порахувати кількість унікальних символів в строці.
# Якщо їх більше 10 - вивести в консоль True, інакше - False. Строку отримати за допомогою функції input()

user_text = input("Please enter something: ")
user_text_uniq = set(user_text)
if len(user_text_uniq) > 10:
    print(True)
else:
    print(False)


# verified_symbols = []
#
# for symbol in set(user_text):
#     if symbol not in verified_symbols:
#         verified_symbols.append(symbol)
#
# unix_symbols = len(verified_symbols)
#
# if unix_symbols > 10:
#     print(True)
# else:
#     print(False)
