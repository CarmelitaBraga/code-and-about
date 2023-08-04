def eh_roteiro(iata, voos, escala):
    escala = escala.split('/')
    for i in range(len(escala) - 1):
        voo = False
        for j in range(len(voos[iata[escala[i]]])):
            if iata[escala[i + 1]] == voos[iata[escala[i]]][j]:
                voo = True
        if not voo: return False
    return True
