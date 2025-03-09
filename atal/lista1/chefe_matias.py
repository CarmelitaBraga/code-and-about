def tempo_total(tempos_pratos):
    if len(tempos_pratos) == 1:
        return tempos_pratos[0]
    elif len(tempos_pratos) == 2:
        return max(int(tempos_pratos[0]), int(tempos_pratos[1]))

    tempos_pratos.sort()
    if len(tempos_pratos) == 3:
        return max(int(tempos_pratos[0])+ int(tempos_pratos[1]), int(tempos_pratos[2]))
    else:
        return min(max(int(tempos_pratos[1]) + int(tempos_pratos[2]), 
                   int(tempos_pratos[3]) + int(tempos_pratos[0])),
                   max(int(tempos_pratos[0]) + int(tempos_pratos[1]) + int(tempos_pratos[2]),
                       int(tempos_pratos[3])))


# tempos_pratos = input().split()
# print(tempo_total(tempos_pratos))
t = int(input())
res = ''
for _ in range(t):
    n = input()
    tempos_pratos = input().split()
    res += str(tempo_total(tempos_pratos)) + '\n'

print(res.strip())