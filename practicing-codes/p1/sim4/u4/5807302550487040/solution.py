lim = int(input())
val = str(input()).split()

soma = 0

for i in range(len(val)):
    if i != len(val)-1:
        if abs(int(val[i+1]) - int(val[i])) > lim:
            soma += 1


print(soma)
