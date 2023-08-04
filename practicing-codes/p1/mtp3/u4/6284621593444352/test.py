def conta_pontos(t1, r, t2):
    soma_t1 = 0
    soma_t2 = 0

    for i in range(3):
        if int(r[0]) > int(r[2]):
            soma_t1 += 3
        
        elif int(r[0]) < int(r[2]):
            soma_t2 += 3

        elif int(r[0]) == r[2]:
            soma_t1 += 1
            soma_t2 += 1

    return soma_t1 and soma_t2

nomes = str(input()).split()
pontos = str(input()).split()

n = int(input())

for jogos in range(n):
    t1, res, t2 = input().split()

    



















partidas = int(input())
for jogo in range(partidas):
    resul = input().split()

#vai dividir a string dos resultados e dar o valor AxB

    for i in range(len(resul[1])):
        if int(resul[1][0]) > int(resul[1][2]):
                    
        elif int(resul[1][0]) < int(resul[1][2]):

        else:



for i in range(len(nomes)):
    

#ligar nomes com pontuação

for i, termo in enumerate(nomes):

#fazer função para dividir os pontos e somar
#resultados iguais ==> lider por ordem alfabetica e lanterna por ultimo

print(f'Líder: {lider}')
print(f'Lanterna: {lanterna}')
