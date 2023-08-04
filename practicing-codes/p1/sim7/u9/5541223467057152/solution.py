def zera_nao_nulos(m, lin, col):
    for i in range(len(m) - 1, -1, -1):
        if m[i][col] != 0:
            m[i][col] = 0
        elif m[i][col] == 0 and i != lin: break
    for j in range(len(m[lin]) - 1, -1, -1):
        if m[lin][j] != 0:
            m[lin][j] = 0
        elif m[lin][j] == 0 and j != col: break
