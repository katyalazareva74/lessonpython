# Требуется вычислить, сколько раз встречается некоторое число X в массиве A[0..N-1]. Пользователь в первой строке вводит
# натуральное число N – количество элементов в массиве. В последующих строках записаны N целых чисел A[i].
# Последняя строка содержит число X

# 5
# 1 2 3 4 5
# 3
# -> 1

n = int(input('Введите количество элементов в массиве: '))
numbers = [0]*n
for i in range(n):
    numbers[i] = int(input(f'{i+1} элемент массива: '))
x = int(input('Введите значение числа X: '))
count = 0
for element in numbers:
    if element == x:
        count += 1
print(f'Количество элементов {n} -> {numbers} -> X = {x} -> {count}')