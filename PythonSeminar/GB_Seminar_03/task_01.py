# Задайте список. Напишите программу, которая определит, присутствует ли в заданном списке строк некое число.

text = ['hsdh', 'dfhsd', 'df', 'dhsdh', 'dhmf', 'dfgjdfj']
search = 'df'

for i in range(len(text)):
    if search in text[i] :
        print(f'В {text[i]}[{i}] - Есть элемент {search}')
    else:
        print(f'В {text[i]}[{i}] - Нет элемента {search}')
