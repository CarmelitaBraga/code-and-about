def acha_e_calcula(categoria, categorias, valores):
    gasto_total = 0
    for i in range(len(categorias)):
        if categoria == categorias[i]:
            gasto_total += valores[i]
    return gasto_total


N = int(input())

gastos = []
valores = []
for _ in range(N):
    categoria, valor = input().split(',')
    gastos.append(categoria)
    valores.append(int(valor))

info = input()

gasto = 0
for e in gastos:
    if info == e:
        gasto = acha_e_calcula(e, gastos, valores)

print(f'R$ {gasto}')
