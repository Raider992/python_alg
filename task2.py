"""
Задание 2.
Ваша программа должна запрашивать пароль
Для этого пароля вам нужно получить хеш, используя функцию sha256
Для генерации хеша обязательно нужно использовать криптографическую соль
Обязательно выведите созданный хеш

Далее программа должна запросить пароль повторно
Вам нужно проверить, совпадает ли пароль с исходным
Для проверки необходимо сравнить хеши паролей

ПРИМЕР:
Введите пароль: 123
В базе данных хранится строка: 555a3581d37993843efd4eba1921f1dcaeeafeb855965535d77c55782349444b
Введите пароль еще раз для проверки: 123
Вы ввели правильный пароль
"""

import hashlib
import uuid

SALT = uuid.uuid4().hex


def hash_pass(pswd):
    return hashlib.sha256(SALT.encode() + pswd.encode()).hexdigest()

def hash_check(hashed_pswd, new_pswd):
    if hashed_pswd == hashlib.sha256(SALT.encode() + new_pswd.encode()).hexdigest():
        return print('Введённый пароль верен')
    else: return print('Упс! Что-то не так')

user_pswd = input('Введите пароль: ')

old_hash = hash_pass(user_pswd)

print(f'Имеем хешированную строку: {old_hash}')

check_pswd = input('Введите пароль ещй раз для проверки')

hash_check(old_hash, check_pswd)
