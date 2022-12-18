# 2. Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них.

my_list = []

for i in range(5):
    number = int(input(f'Введите {i+1} число: '))
    my_list.append(number)

my_max = my_list[0]

for item in my_list:
    if my_max < item:
        my_max = item

print(f'Максимальное значение списка {my_max}')
