def contido(elemento, lista):
    for item in lista:
        if item == elemento:
            return True

def tem_afinidade(l1, l2):
    soma = 0
    for i in range(len(l1)):
        if contido(l1[i], l2):
            soma += 1

    if soma >= 3: return True
    else: return False
