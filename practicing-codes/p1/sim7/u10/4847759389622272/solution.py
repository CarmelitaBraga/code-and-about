elementos = {'H':1, 'S':32, 'O':16, 'C':12, 'Ca':40, 'Na':23, 'P':31}

massa = ''
while True:
    ent = input().split()
    if ent[0] == 'fim': break

    for i in range(len(ent)):
        soma = 0
        if ent[i].isdigit():
            soma += (elementos[ent[i-1]]*int(ent[i]))
            #massa += f'{(elementos[ent[i-1]]*int(ent[i]))}' + '\n'
        elif ent[i] 

print(massa)
