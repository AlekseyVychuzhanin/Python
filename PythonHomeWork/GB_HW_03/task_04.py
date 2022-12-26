# Напишите программу, которая будет преобразовывать десятичное число в двоичное.


num = int(input('Введите число: '))
 
result = ''
 
while num > 0:
    result = str(num % 2) + result
    num = num // 2
 
print(result)