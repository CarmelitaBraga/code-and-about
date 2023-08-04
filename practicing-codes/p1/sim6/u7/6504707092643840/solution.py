def intersecao_listas(lista1, lista2):
    for i in range(len(lista1) - 1, -1, -1):
        iguais = False
        for j in range(len(lista2)):
            if lista1[i] == lista2[j]:
                iguais = True
        if not iguais: lista1.pop(i)
