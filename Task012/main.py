# Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике.
# Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для этого Петя делает две подсказки.
# Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.
# 4 4 -> 2 2
# 5 6 -> 2 3

sum = int(input('Введите сумму задуманных чисел: '))
prod = int(input('Введите произведение задуманных чисел: '))

x = prod*2//sum
y = prod//x

while sum != x+y or prod != x*y:
    x -= 1
    y = prod//x

print(f'X + Y = {sum},   X * Y = {prod} -->  X = {x},  Y = {y}')