# Реализуйте алгоритм перемешивания списка. НЕ ИСПОЛЬЗОВАТЬ ВСТРОЕННЫЕ БИБЛИОТЕКИ SHUFFLE, 
# максимум использование библиотеки Random для и получения случайного int

from random import randint as RI 

my_list = []

for i in range(10):
    i = RI(1, 100)
    my_list.append(i)

print(f'Начальный список: {my_list}')

mix_list = my_list[:]

for i in range(10):
    index_random = RI(1, 9)
    temp = mix_list[i]
    mix_list[i] = mix_list[index_random]
    mix_list[index_random] = temp

print(f'Перемешанный список: {mix_list}')



