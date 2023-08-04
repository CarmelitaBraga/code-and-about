def idiff(seq1, seq2):
    soma = 0
    lis = []
    len_menor = len(seq1) if len(seq1) <= len(seq2) else len(seq2)
    len_maior = len(seq1) if len(seq1) > len(seq2) else len(seq2)
    for i in range(len_menor):
        if seq1[i] != seq2[i]:
            lis.append(i)
        soma += 1
    for j in range(soma, len_maior - soma + 1):
        lis.append(j)
    return lis

a = [1, 2, 3, 4, 6]
b = [2, 2, 3]
print(idiff(a, b))
