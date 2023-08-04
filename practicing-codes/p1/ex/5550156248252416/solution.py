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

print(nomes)
print(horas)

print(menor_hora(nomes, horas))





















'''dados = str(input()).split()
nomes, horas = [], []

def idx_menorhora(horas):
    idx_menor = 0
    for i in range(len(horas)):
        if horas[i] < horas[idx_menor]:
            idx_menor = i
    
    return idx_menor

def main():
    for i in range(0, len(dados), 4):
        nome = dados[i]
        hora = (f'{dados[i+1]}, {dados[i+2]}, {dados[i+3]}')
        nomes.append(nome)
        horas.append(hora)

    idx_vencedor = idx_menorhora(horas)
    vencedor = nomes[idx_vencedor]

    print(i, dados[i], dados[i+1], dados[i+2], dados[i+3])
    print(vencedor)



main()'''
