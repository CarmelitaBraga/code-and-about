def acima_abaixo(lista, m):
    acima = []
    abaixo = []
    for numero in lista:
        if numero > m:
            acima.append(numero)
        elif numero < m:
            abaixo.append(numero)

    return acima, abaixo


def maior_menor(lista):
    menor = lista[-1]
    maior = lista[0]
    for i in range(len(lista)):
        if lista[i] > maior:
            maior = lista[i]
        if lista[i] < menor:
            menor = lista[i]
    return maior, menor

N = int(input())

num_lista = []
for _ in range(N):
    num = int(input())
    num_lista.append(num)

maior, menor = maior_menor(num_lista)
media = abs((maior + menor) / 2)
cima, baixo = acima_abaixo(num_lista, media)

print(f'Menor número: {menor}')
print(f'Maior número: {maior}')
print(f'Média dos extremos: {media:.2f}')
print(f'{len(baixo)} número(s) abaixo da média')
print(f'{len(cima)} número(s) acima da média')
