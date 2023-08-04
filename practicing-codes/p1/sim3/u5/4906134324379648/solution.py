limit = int(input())
soma = 0

while True:
    dados = input().split()

    if dados[0] == '-': break

    for i in range(len(dados)):
        soma += int(dados[i])
        print(f'{dados[i]}', end= ' + ')

    print(end = ' = ')
    print(f'{soma}')

    if soma > 5*limit: break
