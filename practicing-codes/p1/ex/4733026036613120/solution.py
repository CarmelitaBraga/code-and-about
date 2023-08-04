def quanto_tempo(horario1, horario2):
    hora1, min1 = horario1.split(':')
    hora2, min2 = horario2.split(':')
    min1, min2, hora1, hora2 = int(min1), int(min2), int(hora1), int(hora2)
    hora = hora2 - hora1
    if (min2 - min1) < 0:
        hora -= 1
        minn = 60 + (min2 - min1)
    else:
        minn = min2 - min1
    return f'{hora} hora(s) e {minn} minuto(s)'
