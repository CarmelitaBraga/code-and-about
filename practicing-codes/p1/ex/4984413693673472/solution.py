area = float(input())
valor = float(input())
opc = str(input())

calc = area*valor

if opc == 'vista':
    t = calc*0.8
    print(f'Total: R$ {t:.2f}')
elif opc == '2x':
    t = calc*0.9
    print(f'Total: R$ {t:.2f}. Parcelas: R$ {t/2:.2f}')
elif opc == '3x':
    t = calc*0.95
    print(f'Total: R$ {t:.2f}. Parcelas: R$ {t/3:.2f}')
