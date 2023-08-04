peso_congelado = float(input())
peso_descongelado = float(input())

percentagem_agua = 1 - (peso_descongelado / peso_congelado)

if percentagem_agua < 0.05:
    classificacao = 'Produto qualis A'
elif 0.05 <= percentagem_agua < 0.10:
    classificacao = 'Produto em conformidade'
else:
    classificacao = 'Produto não conforme'

print(f'{(percentagem_agua * 100):.1f}% do peso do produto é de água congelada.\n{classificacao}.')