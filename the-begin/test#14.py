'''for c in range(1, 10):
    print(c, end = ' ')
print('\nFIM!')

c = 1
while c < 10:
    print(c)
    c = c + 1
print('FIM!')

r = 'S'
while r == 'S':
    n = str(input('Digite um número: '))
    r = str(input('Quer continuar? ')).upper()
print('Fim!')'''

t = 0
p = 0
i = 0
n = 1
while n != 0:
    n = int(input('Digite um número: '))
    t += n
    if n % 2 == 0:
        p += 1
    else:
        i += 1
print(t, p, i)



