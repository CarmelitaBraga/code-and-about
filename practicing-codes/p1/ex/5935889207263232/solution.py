def diff_simetricos(valores):
    diff = []
    for i in range(len(valores) // 2):
        diff.append(valores[i] - valores[-(i + 1)])

    if len(valores) % 2 != 0:
        diff.append(valores[len(valores) // 2])
    
    return diff
