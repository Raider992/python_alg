"""
Задание 1.

Приведен код, который позволяет сохранить в
массиве индексы четных элементов другого массива

Сделайте замеры времени выполнения кода с помощью модуля timeit

Попробуйте оптимизировать код, чтобы снизить время выполнения
Проведите повторные замеры

Добавьте аналитику: что вы сделали и почему
"""

from random import randint
from timeit import Timer

numbers = []

# for i in range(100):
#     numbers.append(randint(0, 100))
numbers = [el for el in range(1000)]  # Сначала взял массив случайных чисел, но после решил


# забить массив числами по порядку для чистоты эксперимента

def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


def func_2(nums):
    return [i for i, el in enumerate(nums) if el % 2 == 0]


t1 = Timer("func_1(numbers)", "from __main__ import func_1, numbers")
print(t1.timeit(number=1000))

t2 = Timer("func_2(numbers)", "from __main__ import func_2, numbers")
print(t2.timeit(number=1000))

# В принципе, все выводы прозвучали на разборе дз. После оптимизации кода скорость выполнения
# заметно возрастает. Ради интереса попробовал запустить замер на миллионе повторений, но,
# так как сложность у обеих функций линейная, разницы не было.
