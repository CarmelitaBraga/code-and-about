def multiplica_lista(n, lista):
    nova_lista = []
    for vezes in range(n):
        nova_lista += lista

    return nova_lista

dias = ['segunda', 'quarta', 'quinta']
assert multiplica_lista(3, dias) == ['segunda', 'quarta', 'quinta', 'segunda', 'quarta', 'quinta', 'segunda', 'quarta', 'quinta']
