def iterando(palavra):
    uso = iter(palavra)
    next(uso)
    faltas = 0

    if next(uso) == 'f':
        faltas += 1

    return faltas

x = iterando('....fff.f.f.f.f...f.')
print(x)

'''alunos = 0

while True:
    faltas = 0
    p = str(input()).lower()
    
    if p == '-': break

    if iterando(p) == 'f':
        faltas += 1

    if faltas > 8:
        alunos += 1

print(f'{alunos} aluno(s) reprovado(s) por falta.')'''
