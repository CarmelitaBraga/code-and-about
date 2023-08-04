def reducoes(seq):
    lista = []
    for i in range(len(seq) - 1):
        if seq[i] < seq[i + 1]:
            lista.append(0)
        else:
            lista.append(seq[i] - seq[i + 1])
    return lista
