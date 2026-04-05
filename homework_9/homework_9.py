class Rhombus:

    def __init__(self, side_a, angle_a):
        self.side_a = side_a
        self.angle_a = angle_a

    def __setattr__(self, key, value):
        if key == "side_a":
            if value <= 0:
                raise ValueError("Value must be more then 0")
            else:
                super().__setattr__(key, value)
        elif key == "angle_a":
            if value >= 180:
                raise ValueError("Value must be less then 180")
            else:
                super().__setattr__("angle_a", value)

    def angle_b_calculation(self):
        return 180 - self.angle_a


input_data = Rhombus(1, 140)
print(input_data.side_a, input_data.angle_a, input_data.angle_b_calculation())


# Створіть клас геометричної фігури "Ромб". Клас повинен мати наступні атрибути:
#
# сторона_а (довжина сторони a).
# кут_а (кут між сторонами a і b).
# кут_б (суміжний з кутом кут_а).
# Необхідно реалізувати наступні вимоги:
#
# Значення сторони сторона_а повинно бути більше 0.
#
# Кути кут_а та кут_б повинні задовольняти умову: кут_а + кут_б = 180
# Протилежні кути ромба завжди рівні, тому при заданому значенні кут_а, значення кут_б обчислюється автоматично.
# Для встановлення значень атрибутів використовуйте метод __setattr__.
