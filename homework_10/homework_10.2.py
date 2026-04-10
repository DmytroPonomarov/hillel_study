import math
from abc import ABC, abstractmethod

"""
Task_2
Створіть абстрактний клас "Фігура" з абстрактними методами для отримання площі та периметру. 
Наслідуйте від нього декілька (> 2) інших фігур, та реалізуйте математично вірні для них методи для площі та периметру. 
Властивості по типу “довжина сторони” й т.д. повинні бути приватними, та ініціалізуватись через конструктор. 
Створіть Декілька різних об’єктів фігур, та у циклі порахуйте та виведіть в консоль площу та периметр кожної.
"""


class Figure(ABC):
    @abstractmethod
    def area(self): ...

    @abstractmethod
    def perimeter(self): ...


class Foursquare(Figure):
    def __init__(self, side):
        self.__side = side

    def perimeter(self):
        return self.__side * 4

    def area(self):
        return self.__side * self.__side


class Triangle(Figure):
    def __init__(self, side_a, side_b, side_c):
        self.__side_a = side_a
        self.__side_b = side_b
        self.__side_c = side_c

    def perimeter(self):
        return self.__side_a + self.__side_b + self.__side_c

    def area(self):
        p = self.perimeter() / 2
        area = math.sqrt(
            p * (p - self.__side_a) * (p - self.__side_b) * (p - self.__side_c)
        )
        return area


class Rectangular(Figure):
    def __init__(self, side_a, side_b):
        self.__side_a = side_a
        self.__side_b = side_b

    def perimeter(self):
        return (self.__side_a + self.__side_b) * 2

    def area(self):
        return self.__side_a * self.__side_b


figures = [Foursquare(4), Triangle(3, 4, 5), Rectangular(2, 3)]
for figure in figures:
    print(f"{figure.__class__.__name__} perimeter: {figure.perimeter()}")
    print(f"{figure.__class__.__name__} area: {figure.area()}")
