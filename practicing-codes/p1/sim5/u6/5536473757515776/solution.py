def quantos_comeram(N, fila_pedidos):
    serv = 0

    for pedido in fila_pedidos:
        if N >= pedido:
            serv += pedido
            N = N - pedido
        else: break
    
    return serv
