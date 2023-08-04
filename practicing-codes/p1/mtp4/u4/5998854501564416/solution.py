palavras = str(input()).split()

des = 0
ordem = 0
pos = 0

for i in range(len(palavras)):
    if i == len(palavras)-1:
        if palavras[-1] >= palavras[-2]:
            ordem += 1
            #em ordem
        else:
            des += 1
            pos = len(palavras)-1
    else:
        if palavras[i+1] >= palavras[i]:
            ordem += 1
            #em ordem
        else:
            des += 1
            pos = i+1
            break

if des > 0:
    print(f'fora de ordem: {pos+1}')
else:
    print('em ordem')
