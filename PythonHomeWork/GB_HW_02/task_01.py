# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

number = float(input('Введите вещественное число: '))

while number != int(number):
    number *= 10
    # print(number)

sum = 0

while number > 0:
    sum += number % 10
    number //= 10
print(f'Сумма цифр числа = {int(sum)}')
    