alunos = 0

while True:
    faltas = 0
    indice = 0

    p = str(input()).lower()
    indice = (len(p)-1)

    if p == '-': break

    while True:
        if p[indice] == 'f':
            faltas += 1
        if indice == 0: break
        indice -= 1

    if faltas > 8:
            alunos += 1

print(f'{alunos} aluno(s) reprovado(s) por falta.')
