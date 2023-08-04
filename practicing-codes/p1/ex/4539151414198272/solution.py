v1 = str(input())
v2 = str(input())
v3 = str(input())

one = ''

if v1[0] < v2[0] and v1[0] < v3[0]:
    one = v1
    print(f'{one} (1)')
elif v2[0] < v1[0] and v2[0] < v3[0]:
    one = v2
    print(f'{one} (1)')
elif v3[0] < v1[0] and v3[0] < v2[0]:
    one = v3
    print(f'{one} (1)')
elif v1[0] == v2[0] or v1[0] == v3[0]:
    one = v1
    print(f'{one} (2)')
elif v2[0] == v3[0]:
    one = v2
    print(f'{one} (2)')


#mostra nomes repetidos
'''lista = [v1, v2, v3]
soma = 0
for x in range(3):
    if one in lista[x]:
        soma += 1

print(f'{one} ({soma})')'''
