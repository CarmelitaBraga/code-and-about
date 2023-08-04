def idiff(seq1, seq2):
    i = 0
    lista = []
    while True:
        if len(seq1) == 0 or len(seq2) == 0: break
        if seq1[i] != seq2[i]:
            lista.append(i)
        i += 1
        if i == len(seq1) or i == len(seq2): break

    if i < len(seq1):
        for n in range(i, len(seq1)):
            lista.append(n)
    elif i < len(seq2):
        for m in range(i, len(seq2)):
            lista.append(m)
    return lista
