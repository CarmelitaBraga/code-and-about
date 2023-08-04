def idiff(seq1, seq2):
    i = 0
    j = 0
    lis = []
    while i < len(seq1)-1 and i < len(seq2)-1:
        if seq1[i] != seq2[i]:
            lis.append(i)
        i += 1
    if i < len(seq1) or i < len(seq2):
        for x in range(i, len(seq2) - i):
            lis.append(x)
    return lis

a = [1, 2, 3, 4, 6]
b = [2, 2, 3]
print(idiff(a, b))

'''
seq1 = [10, 20, 30, 40, 50, 60, 70]
seq2 = [10, 20, 20, 40, 80]
assert idiff(seq1, seq2) == [2, 4, 5, 6]'''
