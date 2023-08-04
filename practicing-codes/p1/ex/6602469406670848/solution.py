def checa_triplo(e, lista):
    soma = 0
    for elemento in lista:
        if e == elemento:
            soma += 1
    if soma == 3: return True
    else: return False


def acha_e_exclui(e, lista):
    for i in range(len(lista) - 1, -1, -1):
        if lista[i] == e:
            lista.pop(i)
    return lista


def remove_trios(lista):
    for e in lista:
        rem = checa_triplo(e, lista)
        if rem:
            lista = acha_e_exclui(e, lista)
    return lista
