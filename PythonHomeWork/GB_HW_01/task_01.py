# Напишите программу, которая принимает на вход цифру,
# обозначающую день недели, и проверяет, является ли этот день выходным.

a = int(input('Введите цифру, обозначающую день недели: '))

if a > 1 and a < 6:
    print('Нет')
else:
    print('Да')
