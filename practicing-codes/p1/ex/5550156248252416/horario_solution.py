dados = str(input()).split()
nomes, horas = [], []

for i in range(0, len(dados), 4):
    nomes.append(dados[i])
    hora = f'{dados[i+1]}:{dados[i+2]}:{dados[i+3]}'
    horas.append(hora)

def menor_hora(pv, hr):
    menor = 0
    for i in range(len(hr)):
        if hr[i] < hr[menor]:
            menor = i

    venc = pv[menor]
    return venc

print(menor_hora(nomes, horas))
