def maior_menor(lista):
    menor, maior = lista[0], lista[0]
    for i in range(len(lista)):
        if lista[i] > maior:
            maior = lista[i]
        if lista[i] < menor:
            menor = lista[i]
    return maior, menor


def abaixo_acima(media, lista):
    abaixo, acima = 0, 0
    for e in lista:
        if e > media:
            acima += 1
        elif e < media:
            abaixo += 1
    return abaixo, acima


N = int(input())
numeros = []
for _ in range(N):
    numeros.append(int(input()))

maior, menor = maior_menor(numeros)
media = (maior + menor) / 2
abaixo, acima = abaixo_acima(media, numeros)

print(f'Menor número: {menor}')
print(f'Maior número: {maior}')
print(f'Média dos extremos: {media:.2f}')
print(f'{abaixo} número(s) abaixo da média')
print(f'{acima} número(s) acima da média')
