# Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером. Счастливым
# билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех. Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета
# Примеры:
# 385916 -> yes
# 123456 -> no
n = int(input('Введите номер вашего билета: '))
sum = 0
sum1 = 0
n1 = n
sum += n % 10
n = n//10
sum += n % 10
n = n//10
sum += n % 10
n = n//10
sum1 += n % 10
n = n//10
sum1 += n % 10 + n//10
if(sum == sum1):
    print(n1, '-> yes')
else:
    print(n1, '-> no')