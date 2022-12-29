# Создайте словать заданный по формуле 3*n+1, где n это ключ, а формула значение

my_dict = {}

number = int(input('Введите целое число: '))
for n in range(1, number + 1):
    my_dict[n] = 3*n + 1

print(my_dict.get(4, 'Такого ключа нет'))

