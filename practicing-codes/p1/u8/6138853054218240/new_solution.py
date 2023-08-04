def ultimo_maior(lista):
    i_prox = None
    for j in range(len(lista)):
        if lista[j] < 60:
            i_prox = j
            break
    return i_prox


def idosos_inicio(fila):
    for i in range(len(fila)):
        idx = ultimo_maior(fila)
        if fila[i] >= 60 and idx != None:
            fila[i], fila[idx] = fila[idx], fila[i]
