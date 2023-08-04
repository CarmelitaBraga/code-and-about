tt = int(input())

if tt >= 400:
    pag = tt // 400
    resto = tt % 400
    porc = (resto/tt)*100
else:
    pag = 0
    porc = 100

print(f'Serão necessárias {pag} página(s) para visualizar os tweets.')
print(f'{porc:.1f}% dos tweets serão perdidos.')
