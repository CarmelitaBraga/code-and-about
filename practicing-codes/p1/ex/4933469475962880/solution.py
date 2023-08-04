sal = float(input())

cont = sal * 0.12

if sal <= 1317.07:
    imp = sal * 0.08
elif 1317.08 >= sal >= 2195.12:
    imp = sal * 0.09
elif sal > 2195.12:
    imp = sal * 0.11

print(f'O valor da contribuição do INSS a ser pago pelo empregador é de R$ {cont:.2f}')
print(f'O valor da contribuição do INSS a ser pago pelo empregado é de R$ {imp:.2f}')
