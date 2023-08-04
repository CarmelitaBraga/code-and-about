def idosos_inicio(fila):
    for i in range(len(fila)):
        for j in range(i, len(fila)):
            if fila[i] >= 60:
                fila[i], fila[j] = fila[j], fila[i]
    return fila


f = idosos_inicio([25, 33, 67, 61, 35, 8, 12, 15, 22, 63, 75, 30, 34])
print()

o = idosos_inicio([8, 67, 81, 31, 16, 70, 15])
print(o)
