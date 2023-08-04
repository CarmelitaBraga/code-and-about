def lista_so_com_oposto(lista):
    for i in range(len(lista) - 1, -1, -1):
        oposto = False
        for j in range(len(lista)):
            if (lista[i] + lista[j]) == 0:
                oposto = True
        if not oposto: lista.pop(i)
