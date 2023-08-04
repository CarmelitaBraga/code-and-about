def calcula_digitos_verificacao(cpf):
    soma1 = 0
    fator1 = 2
    for num in range(8, -1, -1):
        soma1 += fator1 * int(cpf[num])
        fator1 += 1

    total1 = (soma1*10)%11
    if total1 == 10:
        total1 = 0

    # segunda parte

    soma2 = 2 * total1
    fator2 = 3
    for nume in range(8, -1, -1):
        soma2 += fator2 * int(cpf[nume])
        fator2 += 1

    total2 = (soma2*10)%11
    if total2 == 10:
        total2 = 0
    
    return f'{total1}{total2}'

