"""
2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50). Выведите на экран исходный
и отсортированный массивы.

Пример:
Введите число элементов: 5
Исходный - [46.11436617832828, 41.62921998361278, 18.45859540989644, 12.128870723745806, 8.025098788570562]
Отсортированный - [8.025098788570562, 12.128870723745806, 18.45859540989644, 41.62921998361278, 46.11436617832828]
"""
from copy import copy
from timeit import timeit
import numpy as np

def merge_sort(li):

    try:
        assert len(li) > 1
    except AssertionError:
        print('В массиве должно быть больше 1 элемента')
        quit()

    lst = copy(li)

    def merge(lst):

        if len(lst) > 1:

            mid = len(lst) // 2
            left = lst[:mid]
            right = lst[mid:]

            merge(left)
            merge(right)

            i = j = k = 0

            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    lst[k] = left[i]
                    i += 1
                else:
                    lst[k] = right[j]
                    j += 1
                k += 1

            while i < len(left):
                lst[k] = left[i]
                i += 1
                k += 1

            while j < len(right):
                lst[k] = right[j]
                j += 1
                k += 1

    merge(lst)

    return lst


def gen_list_float(bottom, top, f, size):
    return [float(format(np.random.uniform(bottom,top), f'.{f}f')) for _ in range(size)]


def get_list_el():
    n = int(input('Введите число элементов: '))
    return gen_list_float(0,50,2,n)


li = get_list_el()

li_sorted = merge_sort(li)

print(f'Исходный массив: \n {li}')

print(f'Отсортированный массив: \n {li_sorted}')

print('\n')

li1 = gen_list_float(0,50,2,10)

print('Время работы сортировки 10 элементов: ', timeit("merge_sort(li1)",
    setup="from __main__ import merge_sort, li1", number=1),)

li2 = gen_list_float(0,50,2,100)

print('Время работы сортировки 100 элементов: ', timeit("merge_sort(li2)",
    setup="from __main__ import merge_sort, li2", number=1))

li3 = gen_list_float(0,50,2,10000)

print('Время работы сортировки 10000 элементов: ', timeit("merge_sort(li3)",
    setup="from __main__ import merge_sort, li3", number=1))

