# Дана последовательность чисел. Получить список уникальных элементов заданной последовательности.
'''
data = [1, 2, 3, 4, 1, 3, 5, 7]

my_dict = dict()

for i in range(len(data)):
    my_dict[data[i]] = my_dict.get(data[i], 0) +1
print(my_dict)

new_data = [x[0] for x in my_dict.items() if x[1] == 1]
print(new_data)
'''

my_list = [1, 2, 3, 5, 1, 5, 3, 10]
my_dict = {}

for item in my_list:
    my_dict[item] = my_dict.get(item, 0) + 1
print(my_dict)

for key, value in my_dict.items():
    if value == 1:
        print(key)