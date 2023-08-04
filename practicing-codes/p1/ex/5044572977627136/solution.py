from math import sqrt

while True:
    a = int(input('a? '))
    b = int(input('b? '))
    c = int(input('c? '))

    delta = b**2 - (4 * a * c)

    if delta > 0 and a != 0: break

    print('equação inválida: tente novamente')

x1 = (-b + sqrt(delta)) / (2 * a)
x2 = (-b - sqrt(delta)) / (2 * a)

print(f'{x1:.3f}')
print(f'{x2:.3f}')
