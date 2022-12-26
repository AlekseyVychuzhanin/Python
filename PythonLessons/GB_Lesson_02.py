# colors = ['red', 'green', 'blue']
# data = open('file.txt', 'a')
# data.writelines(colors)
# data.close()

# path = 'file.txt'
# data = open(path, 'r')
# for line in data:
#     print(line)
# data.close()


# import hello
# print(hello.f(1))


# def new_string(symbol, count = 3):
#     return symbol * count
# print(new_string('!', 5))
# print(new_string('!'))
# print(new_string(4))


# Рекурсия (Фибоначчи)
# def fib(n):
#     if n in [1, 2]:
#         return 1
#     else:
#         return fib(n - 1) + fib(n - 2)
# list = []
# for e in range(1, 10):
#     list.append(fib(e))
# print(list)


# Кортежи - неизменяемый список
# a = (3, 4, 5, 6, 7)
# print(a)
# print(a[-1])

# Словари
# dictionary = {}
# dictionary = \
#     {
#         'up': '↑',
#         'left': '←',
#         'down': '↓',
#         'right': '→' 
#     }
# print(dictionary)
# print(dictionary['left'])
# for k in dictionary.keys():
#     print(k)

# Множества
# colors = {'red', 'green', 'blue'}
# print(colors)
# colors.add('red') 
# print(colors)
# colors.add('grey') # Добавление элемента
# print(colors)
# colors.remove('red') # Удаление элемента 
# print(colors)
# # colors.remove('red') # Удаление элемента. Выдаст ошибку потому что элемента не существует 
# colors.discard('red') # Удаление без ошибки
# print(colors) 
# colors.clear() #Очистить множество
# print(colors)

# Списки
# list1 = [1,2,3,4,5]
# list2 = list1
# for e in list1:
#     print(e)
# print()
# for e in list2:
#     print(e)

# list1 [0] = 123