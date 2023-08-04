times = str(input()).split()
pontos = str(input()).split()

jogos = int(input())

def conta_pontos(time1, re, time2):
    r = re.split('x')
    r[0] = int(r[0])
    r[1] = int(r[1])
    if r[0] > r[1]:
        for i in range(len(times)):
            if time1 == times[i]:
                pontos[i] = str(int(pontos[i]) + 3)
    elif r[0] < r[1]:
        for i in range(len(times)):
            if time2 == times[i]:
                pontos[i] = str(int(pontos[i]) + 3)

    elif r[0] == r[1]:
        for i in range(len(times)):
            if time1 == times[i]:
                pontos[i] = str(int(pontos[i]) + 1)

            if time2 == times[i]:
                pontos[i] = str(int(pontos[i]) + 1)

    
    return times, pontos


for jogo in range(jogos):
    t1, resul, t2 = str(input()).split()
    x = conta_pontos(t1, resul, t2)


def define_pos(tms, pts):
    maior = 0
    menor = 0
    lant = ''
    venc = ''
    for j in range(len(tms)):
        pts[j] = int(pts[j])
        if pts[j] > maior:
            maior = pts[j]
            venc = tms[j]
        if pts[j] <= menor or j == 1:
            menor = pts[j]
            lant = tms[j]
    
    return lant, venc

p, v = define_pos(times, pontos)

print(f'Líder: {v}')
print(f'Lanterna: {p}')
