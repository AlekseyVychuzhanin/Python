# Напишите программу, которая будет принимать на вход дробь
# и показывать первую цифру дробной части числа.

number = float(input('Введите дробь: '))

if (int(number) == number):
    print('Нет дробной части')
else:
    print(int(abs(number) * 10) % 10)

# number = input('Введите вещественное число: ')

# number = number.split('.')

# if len(number)>1:
#     print(number[1][0])
# else:
#     print('Число целое')