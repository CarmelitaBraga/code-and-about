from math import ceil

def soma_moldura(m, k):
    tamanho = len(m)
    n_possib = ceil(len(m)/2)
    oposto = -(k + 1) + len(m)
    soma = 0

    if (n_possib - 1) == k and tamanho % 2 != 0:
        soma += m[k][k]
    else:
        for i in range(k, oposto):
            for j in range(k, oposto + 1):
                if i == k:
                    soma += m[i][j]
                    soma += m[oposto][j]
                elif j == k:
                    soma += m[i][j]
                    soma += m[i][oposto]
    return soma
