def scroll(m):
    for i in range(len(m)):
        for j in range(len(m[i])):
            if i < (len(m) - 1):
                m[i][j], m[i - 1][j] = m[i - 1][j], m[i][j]
            else:
                m[i][j] = 0
