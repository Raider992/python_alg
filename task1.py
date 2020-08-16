# 1. Пользователь вводит данные о количестве предприятий, их наименования и прибыль
# за 4 квартала (т.е. 4 отдельных числа) для каждого предприятия. Программа должна определить
# среднюю прибыль (за год для всех предприятий) и вывести наименования предприятий, чья прибыль
# выше среднего и отдельно вывести наименования предприятий, чья прибыль ниже среднего.

from collections import namedtuple

def nt_func():
    companies_number = int(input('Введите число компаний'))
    companies = namedtuple('Income_calc', 'name quarter_1 quarter_2 quarter_3 quarter_4')
    companies_avg_income = {}
    total_income = 0
    higher_inc = []
    lower_inc = []
    equal_inc = []

    for i in range(companies_number):
        company = companies(
            name=input('Введите название компании '),
            quarter_1=int(input('Введите прибыль за первый квартал ')),
            quarter_2=int(input('Введите прибыль за второй квартал ')),
            quarter_3=int(input('Введите прибыль за третий квартал ')),
            quarter_4=int(input('Введите прибыль за четвёртый квартал '))
        )

        companies_avg_income[company.name] = (
                company.quarter_1 + company.quarter_2 + company.quarter_3 + company.quarter_4)/4

    for i in companies_avg_income.values():
        total_income += i
    total_avg_income = total_income / companies_number
    for i, val in companies_avg_income.items():
        if val > total_avg_income:
            higher_inc += [i]
        elif val < total_avg_income:
            lower_inc += [i]
        else:
            equal_inc += [i]

    print(f'Компании с прибылью выше средней: ', '/n')
    for i in higher_inc:
        print(i)

    print(f'Компании с прибылью ниже средней: ', '/n')
    for i in lower_inc:
        print(i)

    print(f'Компании с прибылью равной средней: ', '/n')
    for i in equal_inc:
        print(i)

nt_func()


# Введите число компаний 3
# Введите название компании Крылья
# Введите прибыль за первый квартал 1000
# Введите прибыль за второй квартал 1000
# Введите прибыль за третий квартал 1000
# Введите прибыль за четвёртый квартал 1000
# Введите название компании Лапы
# Введите прибыль за первый квартал 2000
# Введите прибыль за второй квартал 2000
# Введите прибыль за третий квартал 2000
# Введите прибыль за четвёртый квартал 2000
# Введите название компании Хвосты
# Введите прибыль за первый квартал 3000
# Введите прибыль за второй квартал 3000
# Введите прибыль за третий квартал 3000
# Введите прибыль за четвёртый квартал 3000
# Компании с прибылью выше средней:  /n
# Хвосты
# Компании с прибылью ниже средней:  /n
# Крылья
# Компании с прибылью равной средней:  /n
# Лапы