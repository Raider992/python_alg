"""
Задание 1.
Выполните профилирование памяти в скриптах
Проанализировать результат и определить программы с
наиболее эффективным использованием памяти.

Примечание: Для анализа возьмите любые 1-3 ваших программы или несколько
вариантов кода для одной и той же задачи. Можно взять задачи с курса Основ или с текущего курса Алгоритмов

Результаты анализа вставьте в виде комментариев к коду.
Также укажите в комментариях версию Python и разрядность вашей ОС.

ВНИМАНИЕ: ЗАДАНИЯ, В КОТОРЫХ БУДУТ ГОЛЫЕ ЦИФРЫ ЗАМЕРОВ (БЕЗ АНАЛИТИКИ)
БУДУТ ПРИНИМАТЬСЯ С ОЦЕНКОЙ УДОВЛЕТВОРИТЕЛЬНО
"""
from memory_profiler import profile
from random import randint

# Часть 1

@profile
def func_dict(num):
    for a in range(num):
        k = str(a + 1) + ' ' + 'element:'
        d = {k: a}
        return print(d.items())

func_dict(500000)

@profile
def func_lst(num):
    lst = []
    for a in range(num):
        k = str(a + 1) + ' ' + 'element:' + ' a'
        lst.append(k)
        return print(lst)

func_lst(500000)


# Здесь я решил проверить задачу на сравнение быстродействия обработки
# списков и словарей, на сей раз, на потребление памяти. Как и тогда,
# постарался сделать максимально схожие, на мой взгляд(надеюсь, верный), отрезки кода.
# В результате, профилировщик показал, что хотя по быстродействию обработка словаря
# происходит быстрее, чем обработка списка, но память они используют одинаково(по крайней
# мере, насколько может показать профилировщик.
'''
Line #    Mem usage    Increment   Line Contents
================================================
    18     15.3 MiB     15.3 MiB   @profile
    19                             def func_dict(num):
    20     15.3 MiB      0.0 MiB       for a in range(num):
    21     15.3 MiB      0.0 MiB           k = str(a + 1) + ' ' + 'element:'
    22     15.3 MiB      0.0 MiB           d = {k: a}
    23     15.3 MiB      0.0 MiB           return print(d.items())


['1 element: a']
Filename: C:/Users/Work/PycharmProjects/python_alg/task1.py

Line #    Mem usage    Increment   Line Contents
================================================
    27     15.3 MiB     15.3 MiB   @profile
    28                             def func_lst(num):
    29     15.3 MiB      0.0 MiB       lst = []
    30     15.3 MiB      0.0 MiB       for a in range(num):
    31     15.3 MiB      0.0 MiB           k = str(a + 1) + ' ' + 'element:' + ' a'
    32     15.3 MiB      0.0 MiB           lst.append(k)
    33     15.3 MiB      0.0 MiB           return print(lst)



Process finished with exit code 0
'''


#Часть 2

# Здесь я постарался изобразить, опять же, сравнение эффективности функции на рекурсии и
# на цикле. Опять у меня получились идентичные с виду результаты. Вероятно, просто программы
# слишком маленькие и простые, чтобы продемонстрировать работу профилировщика в более полной
# мере, скорее, как я понимаю, он предназначен для оценки более масштабных модулей, как частей
# проекта. В целом, я понял примерно, как работает оценка памяти в питоне, но более детально
# проверить и разобрать работу мемори профайлера мне, к сожалению, не на чем.

value = randint(1000000000,1000000000000)

@profile
def numbers_rec(num, even=0, odd=0):
    if num == 0:
        return print('чётных: ',even, 'нечётных: ', odd)
    else:
        current_number = num % 10
        num = num // 10

        if current_number % 2 == 0:
            even = even + 1
            return numbers_rec(num, even, odd)
        else:
            odd = odd + 1
            return numbers_rec(num, even, odd)


numbers_rec(value)

@profile
def numbers_cycle(num):
    even = odd = 0
    while num > 0:
        if num % 2 == 0:
            even += 1
        else:
            odd += 1
        num = num // 10
    return print("четных - %d, нечетных - %d" % (even, odd))

numbers_cycle(value)

'''
Line #    Mem usage    Increment   Line Contents
================================================
    80     15.9 MiB     15.9 MiB   @profile
    81                             def numbers_rec(num, even=0, odd=0):
    82     15.9 MiB      0.0 MiB       if num == 0:
    83     15.9 MiB      0.0 MiB           return print('чётных: ',even, 'нечётных: ', odd)
    84                                 else:
    85     15.9 MiB      0.0 MiB           current_number = num % 10
    86     15.9 MiB      0.0 MiB           num = num // 10
    87                             
    88     15.9 MiB      0.0 MiB           if current_number % 2 == 0:
    89     15.9 MiB      0.0 MiB               even = even + 1
    90     15.9 MiB      0.0 MiB               return numbers_rec(num, even, odd)
    91                                     else:
    92     15.9 MiB      0.0 MiB               odd = odd + 1
    93     15.9 MiB      0.0 MiB               return numbers_rec(num, even, odd)


четных - 7, нечетных - 5
Filename: C:/Users/Work/PycharmProjects/python_alg/task1.py

Line #    Mem usage    Increment   Line Contents
================================================
    98     15.9 MiB     15.9 MiB   @profile
    99                             def numbers_cycle(num):
   100     15.9 MiB      0.0 MiB       even = odd = 0
   101     15.9 MiB      0.0 MiB       while num > 0:
   102     15.9 MiB      0.0 MiB           if num % 2 == 0:
   103     15.9 MiB      0.0 MiB               even += 1
   104                                     else:
   105     15.9 MiB      0.0 MiB               odd += 1
   106     15.9 MiB      0.0 MiB           num = num // 10
   107     15.9 MiB      0.0 MiB       return print("четных - %d, нечетных - %d" % (even, odd))



Process finished with exit code 0

Стоит отметить, что замер рекурсии повторяется по числу вызовов функции,но 
результат ничем не отличается, так что я не стал копировать лишнее полотно 
полностью идентичного текста
'''

# Часть 3:

# Здесь просто поигрался с генераторами. Видно, что профайлер работает,
# но для мало-мальски различимых значений нужны операции с достаточно масштабными
# объёмами данных

@profile
def some_func():
    val_1 = [str(x) for x in range(100000)]
    del val_1
    val_2 = [x^2 for x in range(100000)]
    del val_2
    return

some_func()

'''
Line #    Mem usage    Increment   Line Contents
================================================
   163     15.9 MiB     15.9 MiB   @profile
   164                             def some_func():
   165     23.5 MiB      0.7 MiB       val_1 = [str(x) for x in range(100000)]
   166     16.0 MiB      0.0 MiB       del val_1
   167     20.2 MiB      0.4 MiB       val_2 = [x^2 for x in range(100000)]
   168     16.0 MiB      0.0 MiB       del val_2
   169     16.0 MiB      0.0 MiB       return
'''