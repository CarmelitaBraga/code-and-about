def sum_of(x):
    return int(x[0]) + int(x[1]) + int(x[2])

a, b = input().split()

sa = sum_of(a)
sb = sum_of(b)
print(max(sa, sb))