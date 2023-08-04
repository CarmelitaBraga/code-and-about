lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim')
for cont in range(0, len(lanche)):
    print(f'Estou comendo {lanche[cont]} na posição {cont}.')

for comida in lanche:
    print(f'Eu vou consumir {comida}.')

for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}.')
print('Comi pra caramba!')

print(sorted(lanche))

#print(lanche[-2])
#lanche[1] = 'Refri' // TypeError: 'tuple' object does not support item assignment
#print(lanche[1:3])
#print(lanche[0:2])

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = b + a
#print(c, f'\nO tamanho é {len(c)}', f'\nO número de 1 é {c.count(1)}')
print(c, c.index(5, 1))   #localiza o num 5 a partir da posição 1

'''pessoa = 'Carmelita', 21, 'F', '52kg'
del(pessoa)
print(pessoa)'''