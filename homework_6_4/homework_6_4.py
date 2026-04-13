# Є ліст з числами, порахуйте сумму усіх ПАРНИХ чисел в цьому лісті
import random

list_1 = [random.randint(1, 100) for x in range(30)]
sum_1 = 0
for num in list_1:
    if num % 2 == 0:
        sum_1 += num
print(sum_1)
