# Требуется вывести все целые степени двойки (т.е. числа вида 2^k), не превосходящие числа N.
# 10 -> 1 2 4 8

n = int(input('Введите натуральное число N: '))
degree2 = str()
num = 1

while num <= n:
    degree2 += str(num) + ' '
    num *= 2
print(n, '-->', degree2)
