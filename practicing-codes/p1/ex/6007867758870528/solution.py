N = int(input())
total_notas = 0
for _ in range(N):
    nota_teste = float(input())
    total_notas += nota_teste

media = total_notas / N

if N == 1:
    print(f'{media:.1f}')
    print('Aluno ainda não aprovado na unidade')
if N == 2:
    print(f'{media:.1f}')
    if media < 6:
        print('Aluno ainda não aprovado na unidade')
    else:
        print('Aluno aprovado na unidade')
if N > 2:
    media = media - 0.5
    print(f'{media:.1f}')
    if media < 6:
        print('Aluno ainda não aprovado na unidade')
    else:
        print('Aluno aprovado na unidade')

