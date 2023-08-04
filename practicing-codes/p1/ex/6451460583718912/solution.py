from math import ceil

prod = input()
hec = float(input())

if prod == 'Fungicida':
    uni = ceil((hec*1)/50)
    tot = uni * 320
    nome = 'Fungicida'
elif prod == 'Herbicida':
    uni = ceil((hec*0.3)/1)
    tot = uni * 100
    nome = 'Herbicida'
elif prod == 'Inseticida':
    uni = ceil((hec*2.5)/30)
    tot = uni * 400
    nome = 'Inseticida'

print(f'{uni} {nome}(s)')
print(f'R$ {tot:.2f}')
