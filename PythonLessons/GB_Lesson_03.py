# def f(x):
#     return x**2

# print(f(4))

# def calc1(x):
#     return x + 10
# # print(calc1(10))

# def calc2(x):
#     return x * 10
# # print(calc2(10))

# def math(op, x):
#     print(op(x))
# math(calc2, 10)
# math(calc1, 10)

# def sum(x, y):
    # return x + y

# sum = lambda x, y: x+y  # Тоже самое, что и def sum

# def mylt(x, y):
#     return x*y

# def calc(op, a, b):
#     print(op(a, b))
#     # return op(a, b)

# calc(sum, 4, 5)


# Создание списка (List Comprehension)

# def f(x):
#     return x**3

# list = [(i, f(i)) for i in range(1, 21) if i % 2 == 0]
# print(list)

# Task 1

# path = '/Users/avych/Desktop/Учеба/Материал/Python/PythonLessons/file.txt'
# f = open(path, 'r')
# data = f.read() + ' '
# f.close()

# numbers = []

# while data != '':
#     space_pos = data.index(' ')
#     numbers.append(int(data[:space_pos]))
#     data = data[space_pos+1:]

# out = []
# for e in numbers:
#     if not e % 2:
#         out.append((e, e**2))
# print(out)

# task 1.2
# def where(f, col):
#     return [x for x in col if f(x)]

# data = '1 2 3 5 8 15 23 38'.split()

# res = map(int, data)
# res = list(filter(lambda x: not x % 2, res))
# res = list(map(lambda x: x**2, res))
# print(res)

# Функция map

# li = [x for x in range(1, 20)]
# li = list(map(lambda x:x+10, li))
# print(li)

# Функция filter

# data = [x for x in range(10)]
# res = list(filter(lambda x: x % 2 == 0, data))
# print(res)

# Функция zip

# users = ['user1', 'user2', 'user3', 'user4', 'user5']
# ids = [4, 5, 19, 14, 7]

# data = list(zip(users, ids))
# print(data)

# Функция enumerate

# users = ['user1', 'user2', 'user3', 'user4', 'user5']
# data = list(enumerate(users))
# print(data)