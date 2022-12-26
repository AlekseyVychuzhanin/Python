# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

my_list1 = [2, 3, 4, 5, 4]
my_list2 = []

for i in range(len(my_list1)):
    if i < len(my_list1)/2:
        num = my_list1[i] * my_list1[len(my_list1) - i - 1]
        my_list2.append(num)
        i +=1

print(f'{my_list1} => {my_list2}')
