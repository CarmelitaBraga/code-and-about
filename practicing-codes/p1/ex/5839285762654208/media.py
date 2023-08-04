nota1 = float(input())
nota2 = float(input())
nota3 = float(input())
peso1 = float(input())
peso2 = float(input())

media = ((nota1*peso1)+(nota2*peso2)+(nota3*(100-peso1-peso2)))/100

print(f'Média Final: {media:.1f}')


