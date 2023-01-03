data_i = input().split()
hora_i = input().split(" : ")

dia_i = int(data_i[1])
horas_i = int(hora_i[0])
minutos_i = int(hora_i[1])
segundos_i = int(hora_i[2])

data_f = input().split()
hora_f = input().split(" : ")

dia_f = int(data_f[1])
horas_f = int(hora_f[0])
minutos_f = int(hora_f[1])
segundos_f = int(hora_f[2])

t_inicio = (horas_i*3600) + (minutos_i*60) + segundos_i
t_final = (horas_f*3600) + (minutos_f*60) + segundos_f

dias_total = dia_f - dia_i

if dias_total == 0:
    tempo_total = t_final - t_inicio
    horas = tempo_total // 3600
    minutos = (tempo_total % 3600) // 60
    segundos = (tempo_total % 3600) % 60
elif dias_total > 0:
    tempo_total = (86400 - t_inicio) + t_final
    if tempo_total < 86400:
        horas = tempo_total // 3600
        minutos = (tempo_total % 3600) // 60
        segundos = (tempo_total % 3600) % 60
        dias_total -= 1
    else:
        horas = tempo_total // 3600
        minutos = (tempo_total % 3600) // 60
        segundos = (tempo_total % 3600) % 60
    if horas == 24:
        horas = 0
    
print(f'{dias_total} dia(s)\n{horas} hora(s)\n{minutos} minuto(s)\n{segundos} segundo(s)')