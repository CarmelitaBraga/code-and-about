def acha_elemento(e, lista):
    for i in range(len(lista)):
        if lista[i] == e:
            return True
    return False


def separa(frequencia):
    variaveis = [0]
    for i in range(len(frequencia)):
        for j in range(len(variaveis)):
            if not acha_elemento(frequencia[i], variaveis):
                variaveis.append(frequencia[i])
    variaveis.pop(0)
    return variaveis


def get_frequencia(frequencia):
    total = []
    variaveis = separa(frequencia)
    for m in range(len(variaveis)):
        soma = 0
        for n in range(len(frequencia)):
            if variaveis[m] == frequencia[n]:
                soma += 1
        total.append(soma)
    return total
