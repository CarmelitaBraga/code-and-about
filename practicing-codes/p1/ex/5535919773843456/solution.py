def inverte(sequencia):
    invertida = ''
    for i in range(len(sequencia) - 1, -1, -1):
        invertida += sequencia[i]
    return invertida


def conta_inversa(palavra):
    inversa = inverte(palavra)
    letras_coinc = 0
    for i in range(len(palavra)):
        if palavra[i] == inversa[i]:
            letras_coinc += 1
    return letras_coinc
    

palavra = input()
soma_letras = conta_inversa(palavra)
print(f'A palavra {palavra} contém {soma_letras} caractere(s) coincidente(s) com a sua inversa.')
