# Задана натуральная степень k. Сформировать случайным образом список коэффициентов
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.

from random import randint as RI

def write_file(name, st):
    with open(name, 'w') as data:
        data.write(st)

def random():
    return RI(0, 101)

def create_polynomial(k):
    my_list = [random() for i in range(k+1)]
    return my_list

def create_str(sp):
    my_list = sp[::-1]
    wr = ''
    if len(my_list) < 1:
        wr = 'x = 0'
    else:
        for i in range(len(my_list)):
            if i != len(my_list) - 1 and my_list[i] != 0 and i != len(my_list) - 2:
                wr += f'{my_list[i]}x^{len(my_list)-i-1}'
                if my_list[i+1] !=0 or my_list[i+2] !=0:
                    wr += ' + '
            elif i == len(my_list) - 2 and my_list[i] != 0:
                wr += f'{my_list[i]}x'
                if my_list[i+1] != 0 or my_list[i+2] !=0:
                    wr += ' + '
            elif i == len(my_list) - 1 and my_list[i] != 0:
                wr += f'{my_list[i]} = 0'
            elif i == len(my_list) - 1 and my_list[i] == 0:
                wr += ' = 0'
    return wr

k1 = int(input('Введите натуральную степень k для первого файла: '))
k2 = int(input('Введите натуральную степень k для второго файла: '))
koef1 = create_polynomial(k1)
koef2 = create_polynomial(k2)
write_file('file_task_01.txt', create_str(koef1))
write_file('file_task_02.txt', create_str(koef2))