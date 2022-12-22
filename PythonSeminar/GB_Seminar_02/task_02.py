# Напишите программу, которая будет на вход принимать число N и выводить числа от -N до N

n = int(input('Введите целое число: '))

# for interval in range(-n, n+1):
#     if interval == n:
#         print(interval)
#     else:
#         print(interval, end = ', ')

my_list = []

for i in range(-n, n + int(abs(n)/n), int(abs(n)/n) ):
    my_list.append(i)

print(*my_list, sep= ', ')