def checa_repetidos(e, matriz):
    soma = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if e == matriz[i][j]: 
                soma += 1
    if soma > 1: return True 
    else: return False


def eh_quadrado_magico(quadrado):
    n = len(quadrado)
    
    somafim = (n + (n**3))/2

    # compara repetidos
    for i in range(n):
        for j in range(n):
            if checa_repetidos(quadrado[i][j], quadrado): return False

    # diagonal principal
    soma = 0
    for i in range(n):
        soma += quadrado[i][i]
    if soma != somafim: return False

    # diagonal secundaria
    soma = 0
    for i in range(n):
        soma += quadrado[i][-(i + 1)]
    if soma != somafim: return False

    # colunas
    for j in range(n):
        soma = 0
        for i in range(n):
            soma += quadrado[i][j]
        if soma != somafim: return False

    # linhas
    for i in range(n):
        soma = 0
        for j in range(n):
            soma += quadrado[i][j]
        if soma != somafim: return False

    return True
