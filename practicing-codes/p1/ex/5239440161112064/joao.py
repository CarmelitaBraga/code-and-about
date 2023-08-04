unit = int(input('Unidade? '))
medi = float(input('Média de aprovação na unidade? '))
print()
if medi >= 7:
    print(f'O aluno vai para a unidade {unit+1} com média {medi:.1f}.')
else:
    print(f'O aluno vai para a unidade {unit} com média {medi:.1f}.')
