"""
Реалізуйте ітератор для зворотного виведення елементів списку.
Напишіть ітератор, який повертає всі парні числа в діапазоні від 0 до N.
"""


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
