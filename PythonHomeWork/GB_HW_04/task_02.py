# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.

def write_file(name, st):
    with open(name, 'w') as data:
        data.write(st)

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

def sqrt_polynomial(k):
    if 'x^' in k:
        i = k.find('^')
        num = int(k[i+1:])
    elif ('x' in k) and ('^' not in k):
        num = 1
    else:
        num = -1
    return num

def k_polynomial(k):
    if 'x' in k:
        i = k.find('x')
        num = int(k[:i])
    return num

def parsing_polynomial(st):
    st = st[0].replace(' ', '').split('=')
    st = st[0].split('+')
    my_list = []
    l = len(st)
    k = 0
    if sqrt_polynomial(st[-1]) == -1:
        my_list.append(int(st[-1]))
        l -= 1
        k = 1
    i = 1
    ii = l - 1
    while ii >= 0:
        if sqrt_polynomial(st[ii]) != -1 and sqrt_polynomial(st[ii]) == i:
            my_list.append(k_polynomial(st[ii]))
            ii -= 1
            i += 1
        else:
            my_list.append(0)
            i += 1

    return my_list

with open('file_task_01.txt', 'r') as data:
    st1 = data.readlines()
with open('file_task_02.txt', 'r') as data:
    st2 = data.readlines()
print(f'Первый многочлен {st1}')
print(f'Второй многочлен {st2}')

my_list1 = parsing_polynomial(st1)
my_list2 = parsing_polynomial(st2)
ll = len(my_list1)
if len(my_list1) > len(my_list2):
    ll = len(my_list2)
new_list = [my_list1[i] + my_list2[i] for i in range(ll)]
if len(my_list1) > len(my_list2):
    mm = len(my_list1)
    for i in range(ll, mm):
        new_list.append(my_list1[i])
else:
    mm = len(my_list2)
    for i in range(ll, mm):
        new_list.append(my_list2[i])
write_file('file_result.txt', create_str(new_list))
with open('file_result.txt', 'r') as data:
    st3 = data.readlines()
print(f'Рузельтат сложения многочленов: {st3}')