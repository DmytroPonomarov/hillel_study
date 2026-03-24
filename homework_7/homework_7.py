# task 1
"""Задача - надрукувати табличку множення на задане число, але
лише до максимального значення для добутку - 25.
Код майже готовий, треба знайти помилки та випраавити\доповнити.
"""

import random


def multiplication_table(number):
    multiplier = 1

    while True:
        result = number * multiplier
        if result > 25:
            break
        print(str(number) + "x" + str(multiplier) + "=" + str(result))

        multiplier += 1


multiplication_table(3)

# task 2
"""Написати функцію, яка обчислює суму двох чисел."""


def sum_calculation():
    a = random.randint(1, 100)
    b = random.randint(1, 100)
    sum_result = a + b
    return sum_result


# task 3
""" Написати функцію, яка розрахує середнє арифметичне списку чисел."""


def arithmetic_mean():
    lst_1 = [random.randint(1, 100) for i in range(1, 100)]
    lst_1_sum = sum(lst_1)
    arithmetic_mean_result = lst_1_sum / len(lst_1)
    return arithmetic_mean_result


# task 4
"""  Написати функцію, яка приймає рядок та повертає його у зворотному порядку."""


def revert_string(text):
    return text[::-1]


user_input = input("Please enter something: ")
reverted_text = revert_string(user_input)

# task 5
"""  Написати функцію, яка приймає список слів та повертає найдовше слово у списку."""


def word_count_1():
    text = input("Please enter something: ")
    single_words = text.split()
    longest_word = max(single_words, key=len)
    return longest_word


# task 6
"""  Написати функцію, яка приймає два рядки та повертає індекс першого входження другого рядка
# у перший рядок, якщо другий рядок є підрядком першого рядка, та -1, якщо другий рядок
# не є підрядком першого рядка."""


def find_substring(str1, str2):
    if str2 in str1:
        return str1.index(str2)
    else:
        return -1


str1 = "Hello, world!"
str2 = "world"
print(find_substring(str1, str2))  # поверне 7

str1 = "The quick brown fox jumps over the lazy dog"
str2 = "cat"
print(find_substring(str1, str2))  # поверне -1


# # task 7
def calculation_even_numbers():
    list_1 = [random.randint(1, 100) for x in range(30)]
    sum_1 = 0
    for num in list_1:
        if num % 2 == 0:
            sum_1 += num
    return sum_1


print(calculation_even_numbers())


# # task 8
def calculation_uniq_characters(text):
    user_text_uniq = set(text)
    return len(user_text_uniq) > 10


user_input = input("Please enter something: ")
result = calculation_uniq_characters(user_input)


# # task 9
def list_unification():
    lst1 = ["1", "2", 3, True, "False", 5, "6", 7, 8, "Python", 9, 0, "Lorem Ipsum"]
    lst2 = []
    for item in lst1:
        if type(item) == str:
            lst2.append(item)
    return lst2


# # task 10


def car_filtering(car_list):
    filtered_list = {
        car: car_data[car]
        for car in car_data
        if car_data[car][1] >= 2017
        and car_data[car][2] >= 1.6
        and car_data[car][-1] <= 36000
    }
    filtered_list_price = {
        brand: details[-1] for brand, details in filtered_list.items()
    }
    sorted_list_price = sorted(filtered_list_price.items(), key=lambda item: item[1])
    first_five_cars = sorted_list_price[:5]
    return first_five_cars


car_data = {
    "Mercedes": ("silver", 2019, 1.8, "sedan", 50000),
    "Audi": ("black", 2020, 2.0, "sedan", 55000),
    "BMW": ("white", 2018, 3.0, "suv", 70000),
    "Lexus": ("gray", 2016, 2.5, "coupe", 45000),
    "Toyota": ("blue", 2021, 1.6, "hatchback", 25000),
    "Honda": ("red", 2017, 1.5, "sedan", 30000),
    "Ford": ("green", 2019, 2.3, "suv", 40000),
    "Chevrolet": ("purple", 2020, 1.4, "hatchback", 22000),
    "Nissan": ("pink", 2018, 1.8, "sedan", 35000),
    "Volkswagen": ("brown", 2021, 1.4, "hatchback", 28000),
    "Hyundai": ("gray", 2019, 1.6, "suv", 32000),
    "Kia": ("white", 2020, 2.0, "sedan", 28000),
    "Volvo": ("silver", 2017, 1.8, "suv", 45000),
    "Subaru": ("blue", 2018, 2.5, "wagon", 35000),
    "Mazda": ("red", 2019, 2.5, "sedan", 32000),
    "Porsche": ("black", 2017, 3.0, "coupe", 80000),
    "Jeep": ("green", 2021, 3.0, "suv", 50000),
    "Chrysler": ("gray", 2016, 2.4, "sedan", 22000),
    "Dodge": ("yellow", 2020, 3.6, "suv", 40000),
    "Ferrari": ("red", 2019, 4.0, "coupe", 500000),
    "Lamborghini": ("orange", 2021, 5.0, "coupe", 800000),
    "Maserati": ("blue", 2018, 4.7, "coupe", 100000),
    "Bugatti": ("black", 2020, 8.0, "coupe", 2000000),
    "McLaren": ("yellow", 2017, 4.0, "coupe", 700000),
    "Rolls-Royce": ("white", 2019, 6.8, "sedan", 500000),
    "Bentley": ("gray", 2020, 4.0, "coupe", 300000),
    "Jaguar": ("red", 2016, 2.0, "suv", 40000),
    "Land Rover": ("green", 2018, 3.0, "suv", 60000),
    "Tesla": ("silver", 2020, 0.0, "sedan", 60000),
    "Acura": ("white", 2017, 2.4, "suv", 40000),
    "Cadillac": ("black", 2019, 3.6, "suv", 55000),
    "Infiniti": ("gray", 2018, 2.0, "sedan", 35000),
    "Lincoln": ("white", 2021, 2.0, "suv", 50000),
    "GMC": ("blue", 2016, 1.5, "pickup", 30000),
    "Ram": ("black", 2019, 5.7, "pickup", 40000),
    "Chevy": ("red", 2017, 2.4, "pickup", 35000),
    "Dodge Ram": ("white", 2020, 3.6, "pickup", 45000),
    "Ford F-Series": ("gray", 2021, 3.5, "pickup", 50000),
    "Nissan Titan": ("silver", 2018, 5.6, "pickup", 35000),
}
print(car_filtering(car_data))


# """  Оберіть будь-які 4 таски з попередніх домашніх робіт та
# перетворіть їх у 4 функції, що отримують значення та повертають результат.
# Обоязково документуйте функції та дайте зрозумілі імена змінним.
# """
