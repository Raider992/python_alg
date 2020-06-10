# 1. Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.

num = int(input("Введите трёхзначное число"))

first_num = num % 10
sec_num = num % 100 // 10
th_num = num // 100

print("Сумма: ", first_num + sec_num + th_num)
print("Произведение: ", first_num * sec_num * th_num)