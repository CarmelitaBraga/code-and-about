def lanchemaispedido(pedidos):
    n = len(pedidos)
    opt = []
    for e in pedidos:
        existe = False
        for el in opt:
            if e == el:
                existe = True
        if not existe: opt.append(e)

    for elemento in opt:
        soma = 0
        for i in range(len(pedidos)):
            if elemento == pedidos[i]:
                soma += 1
        if soma > (n / 2): return elemento
