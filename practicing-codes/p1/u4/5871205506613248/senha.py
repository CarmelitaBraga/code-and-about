senha = input()
soma = 0

for y in senha:
    if y == senha[0]:
        print(y, end='')
    else:
        if y == 'A' or y == 'a':
            y = 4
            soma += 1
        if y == 'O' or y == 'o':
            y = 0
            soma += 1
        if y == 'E' or y == 'e':
            y = 3
            soma += 1
        if y == 'I' or y == 'i':
            y = 1
            soma += 1
        print(y, end = '')
print(f' ({soma} troca(s))')


