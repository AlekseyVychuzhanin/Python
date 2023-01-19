# Задайте список из вещественных чисел. Напишите программу, 
# которая найдёт разницу между максимальным и минимальным значением дробной части элементов, отличной от 0.
import random

'''
my_list = []

for _ in range(10):
    index = random.randint(0, 3)
    my_list.append(round(random.uniform(0, 10), index))
min = (my_list[0] - int(my_list[0]))
max = 0
for i in range(len(my_list)):
    if my_list[i] != int(my_list[i]):
        if (my_list[i] - int(my_list[i])) > max:
            max = (my_list[i] - int(my_list[i])) 
        if (my_list[i] - int(my_list[i])) < min:
            min = (my_list[i] - int(my_list[i]))

'''
index = random.randint(0, 3)
my_list = [round(random.uniform(0, 10), index) for i in range(10)]
new_list = [round(i % 1, 3) for i in my_list if not i % 1 == 0]
dif = max(new_list) - min(new_list)
print(my_list)
print(round(dif, 3))