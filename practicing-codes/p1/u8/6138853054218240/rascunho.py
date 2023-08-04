def meu_insert(pos, e, lista):
    lista.append(e)
    for i in range(len(lista) - 1, pos, -1):
        lista[i], lista[i - 1] = lista[i - 1], lista[i]
    return lista


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
            x = fila.pop(i)
            fila = meu_insert(idx, x, fila)
    return fila

'''
f = idosos_inicio([25, 33, 67, 61, 35, 8, 12, 15, 22, 63, 75, 30, 34])
print(f)

o = idosos_inicio([8, 67, 92, 52, 81, 31, 16, 70, 15])
print(o)

p = idosos_inicio([90, 70, 80, 60, 88])
print(p)

k = idosos_inicio([25, 34, 10, 45, 22, 15, 14])
print(k)

i = idosos_inicio([15, 93, 60])
print(i)'''
