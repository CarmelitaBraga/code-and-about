'''cont = 1
while cont <= 10:
    print(cont, '-->', end = ' ')
    cont += 1
print('Acabou!')'''

'''n = cont = 0
while cont < 3:
    n = int(input('Digite um número: '))
    cont += 1'''

'''x = s = 0
while True:
    x = int(input('Digite um número: '))
    if x == 999:
        break
    s += x
#print('A soma dos número digitados é: {}.'.format(s))
print(f'A soma vale: {s}')'''

x = s = 0
while True:
    x = int(input('Digite um número: '))
    if x == 999:
        break
    s += x
print(f'Fim! \nA soma foi: {s}')