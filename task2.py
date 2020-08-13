"""
Задание 2.

Приведен код, который формирует из введенного числа
обратное по порядку входящих в него цифр.
Задача решена через рекурсию

Сделайте замеры времени выполнения кода с помощью модуля timeit

Попробуйте оптимизировать код, чтобы снизить время выполнения
Проведите повторные замеры

Подсказка: примените мемоизацию

Добавьте аналитику: что вы сделали и почему
"""
from timeit import Timer
from random import randint

def recursive_reverse(number):
    if number == 0:
        return str(number % 10)
    return f'{str(number % 10)}{recursive_reverse(number // 10)}'

num100  = randint(10000, 1000000)
num1000 = randint(1000000, 10000000)
num10000 = randint(100000000, 10000000000000)

t1 = Timer("recursive_reverse(num100)", "from __main__ import recursive_reverse, num100")
print(t1.timeit(number=10000))

t2 = Timer("recursive_reverse(num1000)", "from __main__ import recursive_reverse, num1000")
print(t2.timeit(number=10000))

t3 = Timer("recursive_reverse(num10000)", "from __main__ import recursive_reverse, num10000")
print(t3.timeit(number=10000))

def memoize(f):
    cache = {}

    def decorate(*args):

        if args in cache:
            return cache[args]
        else:
            cache[args] = f(*args)
            return cache[args]
    return decorate

@memoize
def recursive_reverse_m(number):
    if number == 0:
        return ''
    return f'{str(number % 10)}{recursive_reverse_m(number // 10)}'


print('После мемоизации')


t1_m = Timer("recursive_reverse_m(num100)", "from __main__ import recursive_reverse_m, num100")
print(t1_m.timeit(number=10000))

t2_m = Timer("recursive_reverse_m(num1000)", "from __main__ import recursive_reverse_m, num1000")
print(t2_m.timeit(number=10000))

t3_m = Timer("recursive_reverse_m(num10000)", "from __main__ import recursive_reverse_m, num10000")
print(t3_m.timeit(number=10000))

# Тоже был затык с тем, как применить в этой задаче мемоизацию, но после разбора вроде уяснил,
# что к чему.
# Плюсом ещё поразбирался с декораторами. Пока до сих пор не совсем чётко представляю, как
# они работают "под капотом", но прогресс есть. Надеюсь, не фигнёй страдаю с ними =)