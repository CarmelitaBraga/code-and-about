def acha_maior(lis):
    maior = ''
    idx = 0
    for i in range(len(lis)):
        if len(lis[i]) > len(maior) or i == 0:
            maior = lis[i]
            idx = i

    return maior, idx

lista_geral = []

while True:
    lista_pal = []
    while True:
        p = input()

        if p == '---' or p == 'fim': break

        lista_pal.append(p)

    if p == 'fim': break

    elem = acha_maior(lista_pal)
    lista_geral.append(elem[0])

maior_p, idx = acha_maior(lista_geral)

if maior_p != '':
    print(f'Conjunto {idx+1}: {maior_p} ({len(maior_p)} letras)')
