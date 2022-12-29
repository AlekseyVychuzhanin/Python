# Работа со списками и строками

my_string = 'Питон лучший язык в мире'
my_list = ['1','2','34','5','6','7','8']

my_string = my_string.split('и') # Разделяет по символу
my_string = my_string.replace('и', '$') # Меняет символ
print(my_string.lower().startswith('пит')) # Проверяет начало строки

glue = ' '
print(glue.join(my_list)) # Склеивает список


print(my_string)