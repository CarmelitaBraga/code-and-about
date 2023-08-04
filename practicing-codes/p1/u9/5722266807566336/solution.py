def acha(e, lista):
    for i in range(len(lista)):
        if lista[i] == e:
            return i


def filtra_alunos(info_matricula, inscritos, media_min):
    soma = 0
    for i in range(len(info_matricula) - 1, -1, -1):
        contido = False
        for j in range(len(inscritos) - 1, -1, -1):
            if inscritos[j] == info_matricula[i][0]:
                contido = True
        if info_matricula[i][1] < media_min or not contido:
            info_matricula.pop(i)
            soma += 1
    return soma
