# Требуется найти в массиве A[0..N-1] самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих строках записаны N целых чисел A[i]. Последняя строка содержит число X

# 5
# 1 2 3 4 5
# 6
# -> 5

n = int(input('Введите количество элементов в массиве: '))
num = [0]*n

for i in range(n):
    num[i] = int(input(f'{i+1} элемент массива: '))

x = int(input('Введите значение числа X: '))

min1 = num[0]
max1 = num[0]

for i in range(1, n):
    if num[i] > max1:
        max1 = num[i]
    elif num[i] < min1:
        min1 = num[i]

if x <= min1:
    res = min1
elif x >= max1:
    res = max1
else:
    for element in num:
        if element < x:
            if element > min1:
                min1 = element
        else:
            if element < max1:
                max1 = element
    res = min1
    if x-res > max1-x:
        res = max1
print(f'Массив {n} --> {num} --> X = {x} --> Близкое число к X  {res}')