def quantidade_usuarios(cadastro):
    qnt = 0
    for e in cadastro:
        if e != 9999:
            qnt += len(cadastro[e])
    return qnt
