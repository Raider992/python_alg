"""
Задание 3.
Определить количество различных подстрок с использованием хеш-функции.
Дана строка S длиной N, состоящая только из строчных латинских букв.

Подсказка: примените хеши и множества

рара:

рар
ра
ар
ара
р
а
"""
import hashlib
import uuid

SALT = uuid.uuid4().hex

str = input('Введите строку из строчных латинских букв: ')
a = set()

def subs(string,res=['']):
    if len(string) == 0:
        return res
    head, tail = string[0], string[1:]
    res = res + list(map(lambda x: x+head, res))
    return subs(tail, res)

lst = subs(str)
lst.reverse()
lst.pop()

print(lst)
res_lst = []
for i in lst:
    res_lst.append(hashlib.sha256(SALT.encode() + i.encode()).hexdigest())

print(res_lst)