# Требуется определить, можно ли от шоколадки размером n ×m долек отломить k
# долек, если разрешается сделать один разлом по
# прямой между дольками (то есть разломить шоколадку на два прямоугольника).
# Примеры:
# Примечание: каждое считывание производится с новой строки
# 3 2 4 -> yes
# 3 2 1 -> no
n = int(input('Сколько долек имеет шоколадка в длину: '))
m = int(input('Сколько долек имеет шоколадка в ширину: '))
k = int(input('Сколько долек хотите отломить: '))

print(n, m, k, '-> ', ((k % n == 0 or k % m == 0)
      and k < n*m and k != 0) and 'yes' or 'no')
