# Напишите программу, которая принимает на вход координаты двух точек
# и находит расстояние между ними в 2D пространстве.

x1 = float(input('Введите координаты точки A по оси x:'))
y1 = float(input('Введите координаты точки A по оси y:'))
x2 = float(input('Введите координаты точки B по оси x:'))
y2 = float(input('Введите координаты точки B по оси y:'))


distans = round(((x1-x2)**2+(y1-y2)**2)**(1/2),3)

print(f'Растояние от точки A до точки B = {distans}' )