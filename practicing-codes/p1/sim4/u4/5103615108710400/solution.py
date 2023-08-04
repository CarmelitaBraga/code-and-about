palavras = str(input()).split()

total = []

def all_vogais(word):
    somaa = somae = somai = somao = somau = 0
    for e in word:
        if e == 'a':
            somaa += 1
        if e == 'e':
            somae += 1
        if e == 'i':
            somai += 1
        if e == 'o':
            somao += 1
        if e == 'u':
            somau += 1

    if somaa*somae*somai*somao*somau != 0:
        return word

for palavra in palavras:
    total += [all_vogais(palavra)]


s = 0
for x in total:
    if x != None:
        s += 1

print(f'Quantidade de pentavogalicas: {s}')
