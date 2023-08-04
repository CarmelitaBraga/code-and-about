vezes = 0

while True:
    palavra = str(input()).lower()
    
    v = 0
    c = 0

    for letra in palavra:
        if letra in 'aeiou':
            v += 1
        else:
            c += 1

    vezes += 1

    if c > v: break    

print(vezes)
