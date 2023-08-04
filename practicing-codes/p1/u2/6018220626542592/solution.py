from math import ceil

capaci = float(input('Capacidade de revestimento? '))

print(f'\n{" Dados do vão a revestir ":=^29}')
compri = float(input('Comprimento? '))
larg = float(input('Largura? '))
alt = float(input('Altura? '))

area = (2*compri*alt) + (2*larg*alt) + (compri*larg)
cxs = area/capaci

print(f'\n{" Resultados ":=^16}')
print(f'Área total a revestir: {area:.1f} m2')
print(f'Número de caixas: {ceil(cxs)}')
