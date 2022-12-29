# Найдите корни квадратного уравнения Ax² + Bx + C = 0 с помощью математических
# формул нахождения корней квадратного уравнения

equation = '3*x**2 + 5*x - 6 = 0'

print(equation)

equation = equation.replace('*x', '').replace('**2', '').replace(' = 0', '').replace('+ ', '').replace('- ', '-')
equation = equation.split(' ')

# print(equation)

a = int(equation[0])
b = int(equation[1])
c = int(equation[2])

print(f'a = {a}, b = {b}, c = {c}')

disc = b**2 - 4*a*c

if disc < 0:
    print('Корней нет!')
elif disc == 0:
    print(-(b/(2*a)))
else:
    x1 = round((-b + (disc)**0.5)/(2*a), 3)
    x2 = round((-b - (disc)**0.5)/(2*a), 3)
    print(f'x1 = {x1}\nx2 = {x2}')
