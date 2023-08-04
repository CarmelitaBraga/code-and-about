dados = str(input()).split()

lista = []
seq = ''

'''def separa(lista):
    for elemento in lista:
        if elemento'''

for i in range(len(dados)):
    if int(dados[i+1]) <= int(dados[i+5]):
        if int(dados[i+2]) <= int(dados[i+6]):
            if int(dados[i+3]) <= int(dados[i+7]):
                print(dados[i])
            else:
                print(dados[i])
        else:
            print(dados[i])
    else:
        print(dados[i])

''' if i % 4 == 0:
     
        #nome
    if i % 2 != 0:



for i in range(len(dados)):
    if i % 4 == 0:
        lista += dados[i:i+4:1]
        print(lista)
        lista.clear()'''


