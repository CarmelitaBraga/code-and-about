def separa_duas_cores(lista, cor1, cor2):
    for i in range(len(lista)-1, 0, -1):
        for j in range(len(lista)):
            if lista[i] == cor1 and lista[i - 1] == cor2:
                lista[i], lista[j] = lista[j], lista[i]
