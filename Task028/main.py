# Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел.
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.
# 2 2
# 4

def sum_num(a, b):
    if b == 0:
        return a
    return sum_num(a, b-1) + 1


a = int(input('Введите первое число: '))
b = int(input('Введите  второе число: '))
n = 1
if b < 0 and a < 0:
    print(f'Сумма {a} и {b} равна {(sum_num(-a, -b))*-1}')
elif b < 0 and a >= 0:
    print(f'Сумма {a} и {b} равна {sum_num(b, a)}')   
else:
    print(f'Сумма {a} и {b} равна {sum_num(a, b)}')   
