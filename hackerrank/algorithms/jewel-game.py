n = int(input())

l = []
for i in range(n):
    l.append(input())

for w in l:
    count = 0
    i, j = 0, 1
    while j < len(w):
        if w[i] == w[j]:
            w = w[0:j-1] + w[j+1:]
            count+=1
            i, j = 0, 1
        i+=1
        j+=1
    print(count)