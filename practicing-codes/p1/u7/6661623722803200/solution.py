def tem_afinidade(l1, l2):
    soma = 0
    for i in range(len(l1)):
        for j in range(len(l2)):
            if l1[i] == l2[j]:
                soma += 1
    if soma >= 3: return True
    else: return False
