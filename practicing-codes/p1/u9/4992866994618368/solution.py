def busca_matriz(m, e):
    lista = []
    for i in range(len(m)):
        for j in range(len(m[i])):
            if m[i][j] == e:
                lista.append((i,j))
    return lista
