potencia = int(input()) / 1000
tempo = int(input())

tempo_hora = tempo / 60
consumo = tempo_hora * potencia

print(f'{consumo:.1f} kWh')
