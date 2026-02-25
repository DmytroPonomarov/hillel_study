# task 01 == Виправте синтаксичні помилки
print("Hello", end=" ")
print("world!")

# task 02 == Виправте синтаксичні помилки
hello = "Hello"
world = "world"
if True:
    print(f"{hello} {world}!")

# task 03  == Вcтавте пропущену змінну у ф-цію print
for letter in "Hello world!":
    print(letter)

# task 04 == Зробіть так, щоб кількість бананів була завжди в чотири рази більша, ніж яблук
apples = 2
banana = apples * 4
print(f"Кількість бананів: {banana}")

# task 05 == виправте назви змінних
side_1 = 1
side_2 = 2
side_3 = 3
side_4 = 4

# task 06 == Порахуйте периметр фігури з task 05 та виведіть його для користувача
perimeter = side_1 + side_2 + side_3 + side_4
print(f"Периметр дорівнює: {perimeter}")


"""
    # Задачі 07 -10:
    # Переведіть задачі з книги "Математика, 2 клас"
    # на мову пітон і виведіть відповідь, так, щоб було
    # зрозуміло дитині, що навчається в другому класі
"""
# task 07
"""
У саду посадили 4 яблуні. Груш на 5 більше яблунь, а слив - на 2 менше.
Скільки всього дерев посадили в саду?
"""
apple_tree = 4
pear_tree = apple_tree + 5
plum_tree = apple_tree - 2
trees_sum = apple_tree + pear_tree + plum_tree
print(f"Загальна кількість дерев: {trees_sum}")

# task 08
"""
До обіда температура повітря була на 5 градусів вище нуля.
Після обіду температура опустилася на 10 градусів.
Надвечір потепліло на 4 градуси. Яка температура надвечір?
"""
temperature_before_lunch = 5
temperature_after_lunch = temperature_before_lunch - 10
temperature_in_the_evening = temperature_after_lunch + 4
print(f"Температура у ввечері: {temperature_in_the_evening}°C")

# task 09
"""
Взагалі у театральному гуртку - 24 хлопчики, а дівчаток - вдвічі менше.
1 хлопчик захворів та 2 дівчинки не прийшли сьогодні.
Скількі сьогодні дітей у театральному гуртку?
"""
boys_overall = 24
girls_overall = boys_overall / 2
boys_absent_today = 1
girls_absent_today = 2
number_of_children_today = (boys_overall - boys_absent_today) + (
    girls_overall - girls_absent_today
)
print(f"Всього {int(number_of_children_today)} дитини сьогодні")

# task 10
"""
Перша книжка коштує 8 грн., друга - на 2 грн. дороже,
а третя - як половина вартості першої та другої разом.
Скільки будуть коштувати усі книги, якщо купити по одному примірнику?
"""

first_book_price = 8
second_book_price = first_book_price + 2
third_book_price = (first_book_price + second_book_price) / 2
overall_price = first_book_price + second_book_price + third_book_price
print(f"Загальна ціна книжок: {int(overall_price)} грн")
