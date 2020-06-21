# 3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

# У задачи три подзадачи: поиск минимального элемента, поиск максимального и обмен их местами

from random import random

num = 15
arr = [0] * num
for i in range(num):
    arr[i] = int(random() * 100)
    print(arr[i],end=' ')
print()

# Первый вариант через циклы:

mn = 0
mx = 0
for i in range(num):
    if arr[i] < arr[mn]:
        mn = i
    elif arr[i] > arr[mx]:
        mx = i
buffer = arr[mn]
arr[mn] = arr[mx]
arr[mx] = buffer

for i in range(num):
    print(arr[i],end=' ')

# Альтернативный вариант через встроенные функции:
# mn = min(arr)
# mx = max(arr)
# mn_idx = arr.index(mn)
# mx_idx = arr.index(mx)
# print('arr[min]= ',mn,' arr[max]= ',mx)
# arr[imn],arr[imx] = arr[imx],arr[imn]
# for i in range(num):
#     print(arr[i],end=' ')
