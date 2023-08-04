def encontra_menores(num, lista):
    menor = -1
    for termo in lista:
        if int(termo) < num:
            menor = termo
            return menor

    return menor
