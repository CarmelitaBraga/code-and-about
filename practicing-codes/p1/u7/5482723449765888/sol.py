def decrescente(lista):
    for i in range(len(lista)):
        for j in range(len(lista)):
            if lista[i] > lista[j]:
                lista[i], lista[j] = lista[j], lista[i]
    return lista


def slicer(inicio, fim, lista):
    nova_lista = []
    fim = fim if fim <= len(lista) else len(lista)
    for i in range(inicio, fim):
        nova_lista.append(lista[i])
    return nova_lista


def noves_fora(lista):
    final = []
    while True:
        final.append(slicer(0, len(lista), lista))
        if len(lista) == 1 and lista[0] < 9: break

        e2 = lista.pop(1) if len(lista) > 1 else 0
        e1 = lista.pop(0)
        soma = (e1 + e2) % 9
        
        lista.append(soma)
        decrescente(lista)

    return lista[0], final
