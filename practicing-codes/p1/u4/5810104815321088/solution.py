elemento = int(input())
sequencia = str(input()).split()
soma = 0

for i in sequencia:
    if int(i) == elemento:
        soma += 1
        break

if soma >= 1:
    print('sim')
elif soma == 0:
    print('não')
        

