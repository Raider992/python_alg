"""
Задание 1.

Докажите, что словари обрабатываются быстрее, чем списки.

Реализуйте две функции, в первой нужно заполнить элементами список, во второй-словарь
Сделайте замеры времени выполнения каждой из функций

Подсказка: для замеров воспользуйтесь модулем time (см. примеры урока 1)

Примечание: eсли вы уже знаете, что такое декоратор и как его реализовать,
то реализуйте ф-цию-декоратор и пусть она считает время
И примените ее к двум своим функциям.
"""

import time

start_time1 = time.time()

for a in range(1000):
    k = str(a + 1) + ' ' + 'element:'
    d = {k: a}
    print(d.items())

end_time1 = time.time() - start_time1


start_time2 = time.time()
lst = []
for a in range(1000):
    k = str(a + 1)+' '+'element:' + ' a'
    lst.append(k)
    print(lst)

end_time2 = time.time() - start_time2

start_time3 = time.time()
lst = []
for a in range(1000):
    k = str(a + 1)+' '+'element:' + ' a'
    lst[len(lst):] = [k]                 # как альтернатива append
    print(lst)

end_time3 = time.time() - start_time3


print(end_time1)
print(end_time2)
print(end_time3)
print(end_time1 - end_time2)

# В общем, для эксперимента я постарался сделать максимально похожие функции,
# чтобы различие было только в списке и словаре
# В итоге получилось доказать, что словари работают намного быстрее списков
