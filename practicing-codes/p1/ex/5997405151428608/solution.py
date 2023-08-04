num = int(input())
soma = 0
op = num

while True:
    digito = op % 10
    op = op // 10

    soma += digito

    if op // 10 == 0: 
        soma += op%10
        break

dv = soma % 11
if dv == 10:
    print(f'{num}-X')
else:
    print(f'{num}-{dv}')
