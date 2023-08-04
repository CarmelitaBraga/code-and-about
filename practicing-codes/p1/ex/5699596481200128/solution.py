a = input()
b = input()

def menor(p1, p2):
    palavra = p1 if len(p1) <= len(p2) else p2

    return palavra

print('Letras coincidentes')
total = len(a) + len(b)
coin = 0

for i in range(len(menor(a, b))):
    if a[i] == b[i]:
        print(f"'{a[i]}' na posição {i+1}")
        coin += 1

print(f'Total de letras coincidentes: {coin} ({(coin/total)*100:.0f}%)')

