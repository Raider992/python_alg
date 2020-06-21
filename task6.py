# 6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным
# элементами. Сами минимальный и максимальный элементы в сумму не включать.

# 1.Ищем минимальный и максимальный элементы
# 2.Чтобы установить, в какую сторону идти по массиву, меняем индексы местами, если
# индекс максимального элемента будет меньше индекса минимального.
# 3.Ищем сумму элементов

from random import random

el_num = 10
a = [0]*el_num
for i in range(el_num):
    a[i] = int(random()*50)
    print('%3d' % a[i], end='')
print()

min_idx = 0
max_idx = 0
for i in range(1,el_num):
    if a[i] < a[min_idx]:
        min_idx = i
    elif a[i] > a[max_idx]:
        max_idx = i
print(a[min_idx], a[max_idx])

if min_idx > max_idx:
    min_idx, max_idx = max_idx, min_idx

sum = 0
for i in range(min_idx+1, max_idx):
    sum += a[i]
print(sum)