def ultimo_indice(num, lista):
    idx = -1
    for i in range(len(lista)):
        if lista[i] == num:
            idx = i
    return idx
