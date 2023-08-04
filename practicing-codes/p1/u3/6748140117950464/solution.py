prod_congelado = float(input())
prod_descongelado = float(input())

conta = ((prod_congelado-prod_descongelado)/prod_congelado)*100

print(f'{conta:.1f}% do peso do produto é de água congelada.')

if conta < 5.0:
    print('Produto qualis A.')
elif conta < 10.0:
    print('Produto em conformidade.')
else:
    print('Produto não conforme.')
