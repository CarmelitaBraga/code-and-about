def busca(seq, valor):
    idx = -1
    for i in range(len(seq) - 1, -1, -1):
        if valor == seq[i]:
            idx = i
    return idx
