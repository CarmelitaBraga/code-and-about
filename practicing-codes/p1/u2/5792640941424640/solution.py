area = float(input('Área construída? '))
aliquota = float(input('Alíquota? '))

iptu = (area * aliquota) + 35

alt2 = iptu*0.95

print(f'IPTU: R$ {iptu:.2f}\n')

print(f'''Pagamento:
1. Quota única. R$ {iptu*0.75:.2f}
2. Em 6 parcelas. Total: R$ {alt2:.2f}
   6 x R$ {alt2/6:.2f}
3. Em 10 parcelas. Total: R$ {iptu:.2f}
   10 x R$ {iptu/10:.2f}''')
