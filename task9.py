# 9. Найти максимальный элемент среди минимальных элементов столбцов матрицы.

# Проходим каждый столбец, ищем минимальный элемент, потом сравниваем его с переменной, где
# храним максимальный среди минимальных.

from random import random

A = 10
B = 5
a = []
for i in range(B):
    b = []
    for j in range(A):
        n = int(random() * 200)
        b.append(n)
        print('%4d' % n, end='')
    a.append(b)
    print()

mx = -1
for j in range(A):
    mn = 200
    for i in range(B):
        if a[i][j] < mn:
            mn = a[i][j]
    if mn > mx:
        mx = mn
print("Максимальный среди минимальных: ", mx)