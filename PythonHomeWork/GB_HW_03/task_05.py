# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.




num = int(input('Введите размер числа Фибоначчи: '))

if num < 0:
    num = num * -1

fib1 = fib2 = 1

my_list = [fib1, fib2]

for i in range(2, num):
    fib1,fib2 = fib2, fib1 + fib2
    my_list.append(fib2)

fib1=fib2=1

for i in range(-num, 1):
    fib1,fib2 = fib2, fib1 - fib2
    my_list.insert(0, fib2)

print(my_list)