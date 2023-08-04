adulto = int(input())
crianca = int(input())
ingresso = float(input())

total = (adulto * ingresso) + (crianca * (ingresso/2))
print(f'Total: R$ {total:.2f}')
