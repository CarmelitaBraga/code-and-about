'''for c in range(1, 12):
    print('Oi')
    print('FIM')

for c in range(1, 25):
    print(c)
print('FIM')

for c in range(6, 0, -1):
    print(c)
print('FIM')

for c in range(0, 25, 5):
    print(c)

n = int(input('Digite um número inteiro: '))
for c in range(0, n+1):
    print(c)
print('FIM!')

i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
for c in range(i, f+1, p):
    print(c)
print('The end.')'''

s = 0
for c in range(0, 4):
    y = int(input('Digite um número: '))
    s += y                #s = s + y
print('O somatório dos valores foi {}.'.format(s))