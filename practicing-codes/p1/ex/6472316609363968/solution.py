from math import ceil

def soma_moldura(m, k):
    t = len(m)
    n = ceil(len(m)/2)
    soma = 0
    for i in range(n):
        if i == k:
            for j in range(n):
                soma += m[i][j]
                soma += m[-(i + 1)][j]
    for j in range(n):
        if j == k:
            for i in range(n):
                soma += m[i][j]
                soma += m[i][-(j + 1)]
    return soma


################################################

M = [[1,  2,  3,  4 ],
     [5,  6,  7,  8 ],
     [9,  10, 11, 12],
     [14, 15, 16, 17]]
print(M)
print(soma_moldura(M, 1))


M = [[2, 3],
    [4, 1]]
print(M)
print(soma_moldura(M, 0))


M = [[89, 10, 11],
    [31, 25, 70],
    [19, 20, 22]]
print(M)
print(soma_moldura(M, 1))


M = [[0,0,0,0,1],
    [2,0,0,0,0],
    [0,7,0,0,0],
    [0,0,3,0,0],
    [0,0,0,4,0]]
print(M)
print(soma_moldura(M, 0))
print(soma_moldura(M, 1))
print(soma_moldura(M, 2))
