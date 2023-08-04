def calcula_potencia(grandeza, valor, dicionario):
    calculo = 0
    for e in dicionario:
        if e == grandeza:
            calculo = dicionario[f'{e}']*valor
    return calculo


total = []
while True:
    valores = input().split()
    px, py = valores[1], valores[3]
    x, y = float(valores[0]), float(valores[2])
    if x == 0 and y == 0: break

    dic = {'km': 1000, 'hm': 100, 'dam': 10, 'm': 1, 
            'dm': 0.1, 'cm': 0.01, 'mm': 0.001}
    
    resultado = calcula_potencia(px, x, dic) + calcula_potencia(py, y, dic)
    total.append(resultado)    

for _ in range(len(total)):
    print(f'{total[_]:.2f} m')
