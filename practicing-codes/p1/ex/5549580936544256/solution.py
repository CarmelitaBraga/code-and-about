media = 0
termos = 0
soma = 0

while True:
    invest = float(input())

    if invest < media: break

    termos += 1
    soma += invest
    media = soma / termos

print(f'Saldo total do FIS: R${soma:.2f}.')
print(f'Média das contribuições: R${media:.2f}.')
