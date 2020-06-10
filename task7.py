 # 7. По длинам трех отрезков, введенных пользователем, определить возможность существования
 # треугольника, составленного из этих отрезков. Если такой треугольник существует,
 # то определить, является ли он разносторонним, равнобедренным или равносторонним.
 #
 # Треугольник существует, если сумма двух его сторон больше третьей(иначе две стороны сольются с третьей)
 # Если треугольник существует, то сначала проверим на неравенство три его стороны.
 # Если они не равны друг другу, то треугольник разносторонний.
 # Если это не так, то следующим шагом будет проверка на равенство всех сторон треугольника.
 # Если все стороны равны, делается вывод о том, что треугольник равносторонний.
 # Иначе остается только один вариант - равнобедренный треугольник.

print("Введите стороны треугольника")
a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))

if a + b <= c or a + c <= b or b + c <= a:
    print("Треугольник не существует")
elif a != b and a != c and b != c:
    print("Разносторонний")
elif a == b == c:
    print("Равносторонний")
else:
    print("Равнобедренный")