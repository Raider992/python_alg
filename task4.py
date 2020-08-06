"""
4.	Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.

Пример:
Введите количество элементов: 3
Количество элементов - 3, их сумма - 0.75

Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7
"""


def summarize(c, num, el_count, sum):
    if c == el_count:
        return print('Сумма элементов: ', sum)

    elif c < el_count:
        return summarize(c+1, num/2*(-1), el_count, sum + num)

val = int(input('введите n: '))
summarize(0,1,val,0)