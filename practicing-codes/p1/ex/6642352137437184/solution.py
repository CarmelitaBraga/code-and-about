lista_num = []
soma_total = 0

while True:
    num = input()
    if num == 'fim': break
    
    lista_num.append(int(num))
    soma_total += int(num)

media = soma_total / len(lista_num)
print(f'{media:.2f}')

for i in range(len(lista_num)):
    if lista_num[i] < media:
        print(f'{i + 1} {lista_num[i]}')
