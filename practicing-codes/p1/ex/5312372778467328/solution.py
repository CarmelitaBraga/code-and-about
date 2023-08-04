def remove_caracteres(frase, caracteres):
    nova_frase = ''
    for i in range(len(frase)):
        contem = False
        for e in caracteres:
            if frase[i] == e:
                contem = True
        if not contem: nova_frase += frase[i]

    return nova_frase
