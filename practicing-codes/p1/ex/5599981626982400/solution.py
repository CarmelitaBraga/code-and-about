#entrada: 3 notas das unidades, respectivos pesos
#saida: media parcial e nota necessaria na finalpara:
   #aprovado: media final >= 5. aprovado com media final = 7.

#(media final desejada - (media parcial*0.6))/0.4 = nota necessaria

#media parcial = media ponderada das 3 notas

pesos = 0
pond = 0

for x in range(3):
    print(f"{' Estágio {} ':=^16}".format(x+1))
    peso = float(input('Peso? '))
    nota = float(input('Nota? '))
    pesos += peso
    pond += peso*nota

mp = pond/pesos
n5 = (5 - (mp*0.6))/0.4
n7 = (7 - (mp*0.6))/0.4

print(f"{' Resultados ':=^16}")
print(f'Média parcial: {mp:.1f}')
print(f'Nota na final, pra média 5.0 = {n5:.1f}')
print(f'Nota na final, pra média 7.0 = {n7:.1f}')
