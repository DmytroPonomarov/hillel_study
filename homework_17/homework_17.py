"""
Напишіть генератор, який повертає послідовність парних чисел від 0 до N.
Створіть генератор, який генерує послідовність Фібоначчі до певного числа N.
Ітератори:

Реалізуйте ітератор для зворотного виведення елементів списку.
Напишіть ітератор, який повертає всі парні числа в діапазоні від 0 до N.
Декоратори:

Напишіть декоратор, який логує аргументи та результати викликаної функції.
Створіть декоратор, який перехоплює та обробляє винятки, які виникають в ході виконання функції.
"""


def generator_basic(range_number: int):
    for number in (x for x in range(range_number) if x % 2 == 0):
        yield number


def generator_fib(range_number: int):
    a, b = 0, 1
    while a <= range_number:
        yield a
        a, b = b, a + b


class ReverseIterator:
    def __init__(self, data_set):
        self.data = data_set
        self.index = len(self.data) - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < 0:
            raise StopIteration
        else:
            number = self.data[self.index]
            self.index -= 1
            return number


class IteratorEvenNumbers:
    def __init__(self, max_num):
        self.max_num = max_num
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.current <= self.max_num:
            self.current += 1
            if self.current % 2 == 0:
                return self.current
        else:
            raise StopIteration


def logg(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        log = (
            f"Function: {func.__name__}, input data: {args}, {kwargs}, result: {result}\n"
        )
        with open("homework_17_1_log.txt", "a") as file:
            file.write(log)
        return result

    return wrapper


@logg
def sumtwo(a, b):
    sum_result = a + b
    return sum_result


sumtwo(10, 20)


def logg_exc(func):
    def wrapper(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            return result
        except Exception as e:
            log = f"Function: {func.__name__}, error: {type(e).__name__}, input data: {args}, {kwargs}\n"
            with open("homework_17_2_log.txt", "a") as file:
                file.write(log)

    return wrapper


@logg_exc
def sumtwo(a, b):
    sum_result = a + b
    return sum_result


sumtwo("test", 20)
