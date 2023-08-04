def transforma_int(pts):
    for i in range(len(pts)):
        pts[i] = int(pts[i])
    return pts


def conta_pontos(time, grupo, tabela):
    for i in range(len(grupo)):
        if grupo[i] == time:
            tabela[i] += 3
    return tabela


def empate(time1, time2, grupo, tabela):
    for i in range(len(grupo)):
        if grupo[i] == time1:
            tabela[i] += 1
        if grupo[i] == time2:
            tabela[i] += 1
    return tabela


def acha_vencedor_lanterna(times, pontos):
    idx_maior = 0
    idx_menor = 0
    for j in range(len(times)):
        if pontos[j] > pontos[idx_maior]:
            idx_maior = j
        if pontos[j] <= pontos[idx_menor]:
            idx_menor = j
    return idx_maior, idx_menor


times = input().split()
pontos = transforma_int(input().split())
n_jogos = int(input())

for _ in range(n_jogos):
    resultado = input().split()
    p_time1, p_time2 = resultado[1].split('x')
    
    if p_time1 == p_time2:
        pontos = empate(resultado[0], resultado[2], times, pontos)
    elif p_time1 > p_time2:
        pontos = conta_pontos(resultado[0], times, pontos)
    elif p_time1 < p_time2:
        pontos = conta_pontos(resultado[2], times, pontos)
        
v, l = acha_vencedor_lanterna(times, pontos)

print(f'Líder: {times[v]}')
print(f'Lanterna: {times[l]}')
