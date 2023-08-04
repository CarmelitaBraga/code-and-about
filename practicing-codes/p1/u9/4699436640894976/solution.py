def diagonais(M):
    d = [[],[]]
    for i in range(len(M)):
        d[0].append(M[i][i])
        d[1].append(M[i][-(i+1)])
    return d
