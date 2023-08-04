num = int(input())
lista_num = []

def reverso(lista):
    for i in range(len(lista) // 2):
        lista[i], lista[-(i + 1)] = lista[-(i + 1)], lista[i]
    return lista

if num == 00000:
    print(f'00000')
else:
    while num // 10 != 0:
        x = num % 10
        lista_num.append(x)
        num = num // 10

    lista_num.append(num)
    nova_lista = reverso(lista_num)

    soma_pares = nova_lista[0] + nova_lista[2] + nova_lista[4]
    soma_impares = nova_lista[1] +  nova_lista[3]

    somatorio = soma_pares * soma_impares

    print(f'{somatorio:0>5}')
