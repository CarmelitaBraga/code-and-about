def diferenca_listas(lista1, lista2):
    for i in range(len(lista1) - 1, -1, -1):
        for j in range(len(lista2)):
            if i < len(lista1) and lista1[i] == lista2[j]:
                lista1.pop(i)
    return lista1


'''x = diferenca_listas([1, 2, 3, 4], [2, 4])
print(x)

y = diferenca_listas([-1, 0, 1], [3])
print(y)

z = diferenca_listas([9, 5, 6, 3, 49], [5, 49, 9, 3, 6])
print(z)'''
