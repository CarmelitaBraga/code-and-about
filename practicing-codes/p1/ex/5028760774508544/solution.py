#acima do limite


lim = int(input())

lin = ''
while True:
    lista = str(input()).split()
    if lista[0] == '-': break
    
    soma = 0
    for num in lista:
        soma += int(num)

    for i in range(len(lista)):
        if soma >= lim:
            if i == len(lista) - 1:
                lin += lista[-1] + ' = ' + str(soma) + '\n'
            else:
                lin += lista[i] + ' + '

    if soma > 5*lim: break

print(lin, end='')
