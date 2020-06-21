# 5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и индекс.

# Создаём переменную idx для хранения индекса, изначально ставим ей значение вне обычной индексации,
# делаем это с целью определения, были ли в массиве отрицательные элементы. Потом перебираем массив 
# в цикле. Если очередной элемент меньше нуля и значение переменной idx равно -1, то значит, это первый
# встретившийся отрицательный элемент. Запоминаем его индекс в переменной idx. Если же очередной
# элемент отрицательный, но idx уже не содержит -1, то сравниваем значение текущего элемента
# с тем, которое содержится по индексу, хранимому в idx. Если текущий элемент больше, то
# записываем его индекс в idx.

from random import random

el_num = 15
arr = []
for i in range(el_num):
    arr.append(int(random() * 100) - 50)
print(arr)

i = 0
idx = -1
while i < el_num:
    if arr[i] < 0 and idx == -1:
        idx = i
    elif arr[i] < 0 and arr[i] > arr[idx]:
        idx = i
    i += 1

print(idx + 1, ':', arr[idx])