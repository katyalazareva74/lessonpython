# Даны два неупорядоченных набора целых чисел (может быть, с повторениями). Выдать без повторений в порядке возрастания
# все те числа, которые встречаются в обоих наборах. Пользователь вводит 2 числа. n - кол-во элементов первого множества.
# m - кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.

# 11 6
# 2 4 6 8 10 12 10 8 6 4 2
# 3 6 9 12 15 18

# 6 12

n = int(input('Введите количество элементов в первом наборе: '))
num1 = [0]*n
for i in range(n):
    num1[i] = int(input(f'{i+1} элемент набора: '))
m = int(input('Введите количество элементов во втором наборе: '))
num2 = [0]*m
for i in range(m):
    num2[i] = int(input(f'{i+1} элемент набора: '))

print(n,m,'\n',*num1,'\n',*num2)

num1 = set(num1)
num2 = set(num2)
num1.intersection_update(num2)
num1 = list(num1)
num1.sort()
print(*num1, sep=' ')
