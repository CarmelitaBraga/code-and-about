a = [1, 7, 4, 25, 13]
b = a                      #ligação entre eles
c = a[:]                   #pura cópia de a
b[1] = 2
print(f'Lista A: {a}')
print(f'Lista B: {b}')
print(f'Lista C: {c}')


'''valor = list()    #ou: valor = []
valor.append(5)
valor.append(2)
valor.append(1)
for v in valor:
    print(f'{v}... ', end = '')
for cont in range(0, 5):
    valor.append(int(input('Digite um número: ')))
for tex, vex in enumerate(valor):
    print(f'Na posição {tex}, temos o {vex}.')'''


'''num = [2, 5, 9, 1]
print(num)
num[1] = 3
print(num)
num.append(4)
print(num)
num.insert(2, 10)
print(num)
num.sort()
print(num)
del num[2]
print(num)
num.pop()
print(num)
num.insert(2, 99)
print(num)
num.append(8)
num.append(56)
num.append(45)
num.insert(7, 1)
print(num)
num.remove(99)
print(num)
num.pop(6)
print(num)
num.sort(reverse=True)
print(num)
print(len(num))'''


import math
x = int(input('Quadrados preenchidos: '))
a = 0
for c in range(1, x + 1):
    y = math.pow(2, c)
    a += y
print(f'A soma total é {a} grãos.')