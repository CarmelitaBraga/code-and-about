# TODO: função com efeito colateral

def matriz_menor(M1, M2):
    M3 = []
    for i in range(len(M1)):
        M3.append([])
        for j in range(len(M1[i])):
            if M1[i][j] <= M2[i][j]:
                M3[i].append(M1[i][j])
            else:
                M3[i].append(M2[i][j])
    return M3
