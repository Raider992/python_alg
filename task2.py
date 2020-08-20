"""
Задание 2.
Предложить варианты оптимизации и доказать (наглядно, кодом) их эффективность
"""
from memory_profiler import memory_usage

# Вариант 1(свой, решил использовать memory_usage вместо готового декоратора из profile):


def func1():
    m1 = memory_usage()
    print(f'm1 = {m1}')
    val_1 = [x^2 for x in range(1000000)]
    val_2 = []
    m2 = memory_usage()
    print(f'm2 = {m2}')
    for i in val_1:
        val_2.append(i*2)
    val_12 = val_1 + val_2
    m3 = memory_usage()
    print(f'm3 = {m3}')
    val_3 = [str(x) for x in range(100000)]
    m4 = memory_usage()
    print(f'm4 = {m4}')
    for i in range(20000):
        val_3.append(str(i))
    m5 = memory_usage()
    print(f'm5 = {m5} \n')
    return

func1()


def func1_opt():
    m1 = memory_usage()
    print(f'm1 = {m1}')
    val_1 = [x^2 for x in range(1000000)]
    val_2 = []
    m2 = memory_usage()
    print(f'm2 = {m2}')
    for i in val_1:
        val_2.append(i*2)
    val_12 = val_1 + val_2
    m3 = memory_usage()
    print(f'm3 = {m3}')
    del val_1
    del val_2
    del val_12
    m3_1 = memory_usage()
    print(f'm3_1 = {m3_1}')
    val_3 = [str(x) for x in range(100000)]
    m4 = memory_usage()
    print(f'm4 = {m4}')
    for i in range(20000):
        val_3.append(str(i))
    m5 = memory_usage()
    print(f'm5 = {m5}')
    del val_3
    m6 = memory_usage()
    print(f'm6 = {m6}')
    return

func1_opt()

'''
m1 = [14.9609375]
m2 = [53.640625]
m3 = [107.578125]
m4 = [115.8828125]
m5 = [117.28515625] 

m1 = [17.0]
m2 = [54.953125]
m3 = [108.2578125]
m3_1 = [16.953125]
m4 = [22.72265625]
m5 = [24.0703125]
m6 = [16.828125]

Process finished with exit code 0

'''

# В этом примере наглядно показана польза от удаления отработанных переменных и
# очистки участков памяти, с которыми больше не планируется работать.

# Вариант 2:

# Вариант с декоратором, взятым из разбора дз. Сделал ради усреднённого замера памяти
# вместо одиночных измерений с помощью memory_usage

def memory_check(func):
    def start(*args, **kwargs):

        mem_diff = []
        for i in range(5):
            m1 = memory_usage()
            print(f'm1 - {m1}')

            func(args[0])

            m2 = memory_usage()
            print(f'm2 - {m2}')

            mem_diff.append(m2[0] - m1[0])

        print(f'{sum(mem_diff)/5} Mib')
    return start

@memory_check
def func2(val):
    val_1 = [x^2 for x in range(val)]
    val_2 = []
    for i in val_1:
        val_2.append(i*2)
    val_3 = [str(x) for x in range(100000)]
    for i in range(20000):
        val_3.append(str(i))
    return print('\n')

func2(1000000)

@memory_check
def func2_opt(val):
    val_1 = [x^2 for x in range(val)]
    val_2 = []
    for i in val_1:
        val_2.append(i*2)
    del val_1
    del val_2
    val_3 = [str(x) for x in range(100000)]
    for i in range(20000):
        val_3.append(str(i))
    del val_3
    return print('\n')

func2_opt(1000000)

'''
m1 - [14.96484375]


m2 - [16.00390625]
m1 - [16.00390625]


m2 - [16.0234375]
m1 - [16.0234375]


m2 - [16.00390625]
m1 - [16.00390625]


m2 - [16.0234375]
m1 - [16.0234375]


m2 - [16.00390625]
0.2078125 Mib
m1 - [16.00390625]


m2 - [16.0234375]
m1 - [16.0234375]


m2 - [16.00390625]
m1 - [16.00390625]


m2 - [16.0234375]
m1 - [16.0234375]


m2 - [16.00390625]
m1 - [16.00390625]


m2 - [16.0234375]
0.00390625 Mib

Process finished with exit code 0

'''

# В итоге тоже видно разницу значений памяти, теперь усреднённых