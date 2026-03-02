import math

# task 01 == Розділіть змінну alice_in_wonderland так, щоб вона займала декілька фізичних лінії
# task 02 == Знайдіть та відобразіть всі символи одинарної лапки (') у тексті
# task 03 == Виведіть змінну alice_in_wonderland на друк

# task_01
alice_in_wonderland = """
    "Would you tell me, please, which way I ought to go from here?"
    "That depends a good deal on where you want to get to," said the Cat.
    "I don't much care where ——" said Alice.
    "Then it doesn't matter which way you go," said the Cat.
    "—— so long as I get somewhere," Alice added as an explanation.
    "Oh, you're sure to do that," said the Cat, "if you only walk long enough."
    """

# task_02 --- Я не дуже зрозумів сенс оригинальної задачі типу просто познаходити апострофи і вивести їх,
#            вирішив зробити зі словами.
words_with_apostrophe = []
single_words = alice_in_wonderland.split(" ")
for word in single_words:
    if "'" in word:
        words_with_apostrophe.append(word)
search_result = ", ".join(words_with_apostrophe)
print(f"\nУ тексті апостроф знайденний у таких словах: {search_result}.")

# task_02 --- Як оригінальна задача каже.
for apostrophe in alice_in_wonderland:
    if apostrophe == "'":
        print(f"\n{apostrophe}")

# task_03
print(f"\nТекст казки: {alice_in_wonderland}")


# task 04
"""
Площа Чорного моря становить 436 402 км2, а площа Азовського
моря становить 37 800 км2. Яку площу займають Чорне та Азов-
ське моря разом?
"""
black_sea_area = 436402
azov_sea_area = 37800
print(
    f"\nЗагальна площа Азовського і Чорного морів становить {azov_sea_area + black_sea_area} км2."
)

# task 05
"""
Мережа супермаркетів має 3 склади, де всього розміщено
375 291 товар. На першому та другому складах перебуває
250 449 товарів. На другому та третьому – 222 950 товарів.
Знайдіть кількість товарів, що розміщені на кожному складі.
"""
total_number_of_goods = 375291
total_warehouse_1_and_2 = 250449
total_warehouse_2_and_3 = 222950
warehouse_1 = total_number_of_goods - total_warehouse_2_and_3
warehouse_2 = total_warehouse_1_and_2 - warehouse_1
warehouse_3 = total_warehouse_2_and_3 - warehouse_2
assert total_number_of_goods == (warehouse_1 + warehouse_2 + warehouse_3)

print(
    f"\nКількість товарів на першому складі складає {warehouse_1}. \n"
    f"Кількість товарів на другому складі складає {warehouse_2}. \n"
    f"Кількість товарів на третьому складі складає {warehouse_3}."
)


# task 06
"""
Михайло разом з батьками вирішили купити комп’ютер, ско-
риставшись послугою «Оплата частинами». Відомо, що сплачу-
вати необхідно буде півтора року по 1179 грн/місяць. Обчисліть
вартість комп’ютера.
"""
monthly_payment = 1179
payment_period_years = 1.5
payment_period_months = int(payment_period_years * 12)
print(f"\nВартість комп’ютера складає {payment_period_months * monthly_payment} грн")

# task 07
"""
Знайди остачу від діленя чисел:
a) 8019 : 8     d) 7248 : 6
b) 9907 : 9     e) 7128 : 5
c) 2789 : 5     f) 19224 : 9
"""
a = (8019 / 8) % 1
b = (9907 / 9) % 1
c = (2789 / 5) % 1
d = (7248 / 6) % 1
e = (7128 / 5) % 1
f = (19224 / 9) % 1
results = (a, b, c, d, e, f)

print(
    f"\nЗалишок у задачах\n"
    f"a = {a:.3g} \n"
    f"b = {b:.3g} \n"
    f"c = {c:.3g} \n"
    f"d = {d:.3g} \n"
    f"e = {e:.3g} \n"
    f"f = {f:.3g}"
)

# task 08
"""
Іринка, готуючись до свого дня народження, склала список того,
що їй потрібно замовити. Обчисліть, скільки грошей знадобиться
для даного її замовлення.
Назва товару    Кількість   Ціна
Піца велика     4           274 грн
Піца середня    2           218 грн
Сік             4           35 грн
Торт            1           350 грн
Вода            3           21 грн
"""
big_pizza_price = 274
mid_size_pizza_price = 218
juice_price = 35
cake_price = 350
water_price = 21
print(
    f"\nУсе замовлення Ірини коштує {((big_pizza_price * 4) + (mid_size_pizza_price * 2) + (juice_price *4) + 
                                    cake_price + (water_price *3))} грн"
)

# task 09
"""
Ігор займається фотографією. Він вирішив зібрати всі свої 232
фотографії та вклеїти в альбом. На одній сторінці може бути
розміщено щонайбільше 8 фото. Скільки сторінок знадобиться
Ігорю, щоб вклеїти всі фото?
"""
overall_photo_amount = 232
max_album_page_size = 8
print(
    f"\nІгорю знадобиться {math.ceil(overall_photo_amount / max_album_page_size)} пустих сторінок у альбомі"
)


# task 10
"""
Родина зібралася в автомобільну подорож із Харкова в Буда-
пешт. Відстань між цими містами становить 1600 км. Відомо,
що на кожні 100 км необхідно 9 літрів бензину. Місткість баку
становить 48 літрів.
1) Скільки літрів бензину знадобиться для такої подорожі?
2) Скільки щонайменше разів родині необхідно заїхати на зап-
равку під час цієї подорожі, кожного разу заправляючи пов-
ний бак?
"""

road_distance = 1600
fuel_consumption_100_km_gas = 9
car_tank_max_capacity = 48

print(
    f"\nВсього {(fuel_consumption_100_km_gas / 100) * road_distance} літра/літрів бензину знадобиться для подорожі"
    f"\nПовний бак потрібно будет заправити {math.ceil(((fuel_consumption_100_km_gas / 100) 
                                                          * road_distance) / car_tank_max_capacity)} рази"
)
