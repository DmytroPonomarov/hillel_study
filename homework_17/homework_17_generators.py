"""
Напишіть генератор, який повертає послідовність парних чисел від 0 до N.
Створіть генератор, який генерує послідовність Фібоначчі до певного числа N.
"""


def generator_basic(range_number: int):
    for number in (x for x in range(range_number) if x % 2 == 0):
        yield number


def generator_fib(range_number: int):
    a, b = 0, 1
    while a <= range_number:
        yield a
        a, b = b, a + b
