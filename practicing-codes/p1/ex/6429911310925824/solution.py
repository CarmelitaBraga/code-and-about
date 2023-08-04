vzs = int(input())
par = 0
impar = 0
soma_par = 0
soma_impar = 0

for r in range(vzs):
    num = int(input())
    if num % 2 == 0:
        par += 1
        soma_par += num
    else:
        impar += 1
        soma_impar += num

media_p = soma_par/par
media_i = soma_impar/impar
print(f'pares: {par}')
print(f'ímpares: {impar}')
print(f'média pares: {media_p:.1f}')
print(f'média ímpares: {media_i:.1f}')
