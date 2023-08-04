import math

print('Cálculo da Superfície de um Cilindro')
print('---')
diametro = float(input('Medida do diâmetro? '))
altura = float(input('Medida da altura? '))

area = (altura * (diametro/2) * 2 * math.pi) + 2 * math.pi * (diametro/2)**2

print('---')
print(f'Área calculada: {area:.2f}')


