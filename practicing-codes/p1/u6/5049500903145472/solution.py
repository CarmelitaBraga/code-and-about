def maioridade_penal(nomes, idades):
    nomes = str(nomes).split()
    idades = str(idades).split()

    maiores = ''
    for i in range(len(nomes)):
        if int(idades[i]) >= 18:
            maiores += nomes[i] + ' '

    return maiores.strip()


