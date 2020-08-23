"""
1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100). Выведите на экран
исходный и отсортированный массивы. Сортировка должна быть реализована в
виде функции. Обязательно доработайте алгоритм (сделайте его умнее).

Идея доработки: если за проход по списку не совершается ни одной сортировки,
то завершение
Обязательно сделайте замеры времени обеих реализаций
и обосновать дала ли оптимизация эффективность

Подсказка: обратите внимание, сортируем не по возрастанию, как в примере,
а по убыванию
"""
import timeit
from random import randint
import copy


orig_list = [randint(-100,100) for _ in range(20)]
orig_list2 = copy.deepcopy(orig_list) # Глубокое копирование, чтобы не сортировать
                                      # один и тот же список

orig_list_large = [randint(-100,100) for _ in range(5000)]
orig_list_large2 = copy.deepcopy(orig_list_large)

print(orig_list)
print(orig_list2, '\n')

def reverse_bubble(li):
    lst = copy.copy(li)
    n = len(lst)
    while(n > 1):
        for j in range(len(lst) - 1, 0, -1):
            if lst[j] > lst[j-1]:
                lst[j], lst[j-1] = lst[j-1], lst[j]
        n -= 1
    return lst


def reverse_bubble_opt(li):
    lst = copy.copy(li)
    update = True
    n = len(lst)
    while(update and n > 1):
        update = False
        for j in range(len(lst) - 1, 0, -1):
            if lst[j] > lst[j-1]:
                lst[j], lst[j-1] = lst[j-1], lst[j]
                update = True
    return lst


sorted_list = reverse_bubble(orig_list)
sorted_list2 = reverse_bubble_opt(orig_list2)

print(sorted_list)
print(sorted_list2, '\n')

print('Измерения времени выполнения:\n')

print('Для маленьких списков:')

print('Не оптимизированная: ', timeit.timeit("reverse_bubble(orig_list)", \
    setup="from __main__ import reverse_bubble, orig_list", number=10))

print('Оптимизированная: ', timeit.timeit("reverse_bubble_opt(orig_list2)", \
    setup="from __main__ import reverse_bubble_opt, orig_list2", number=10), '\n')

print('Для больших списков:')

print('Не оптимизированная: ', timeit.timeit("reverse_bubble(orig_list_large)", \
    setup="from __main__ import reverse_bubble, orig_list_large", number=10))

print('Оптимизированная', timeit.timeit("reverse_bubble_opt(orig_list_large2)", \
    setup="from __main__ import reverse_bubble_opt, orig_list_large2", number=10))

'''
[-34, -48, -80, -8, 89, -50, -41, 0, -18, -47, 1, 80, -71, 33, 13, -9, -34, -70, 24, -43]
[-34, -48, -80, -8, 89, -50, -41, 0, -18, -47, 1, 80, -71, 33, 13, -9, -34, -70, 24, -43] 

[89, 80, 33, 24, 13, 1, 0, -8, -9, -18, -34, -34, -41, -43, -47, -48, -50, -70, -71, -80]
[89, 80, 33, 24, 13, 1, 0, -8, -9, -18, -34, -34, -41, -43, -47, -48, -50, -70, -71, -80] 

Измерения времени выполнения:

Для маленьких списков:
Не оптимизированная:  0.0009263000000000049
Оптимизированная:  0.0007169999999999954 

Для больших списков:
Не оптимизированная:  27.370464600000002
Оптимизированная 26.80808

Process finished with exit code 0


'''