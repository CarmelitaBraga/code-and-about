from math import inf

n = input()

def is_valid(cur):
    sete, quatro = 0, 0
    for i in range(len(cur)):
        if cur[i] == '7':
            sete += 1
        if cur[i] == '4':
            quatro += 1

    return sete == quatro

def generate_permutations(cur, n, combs):
    if len(cur) == n:  # Base case: When sequence reaches length n
        if is_valid(cur):
            combs.add(cur)
        return

    generate_permutations(cur + '7', n, combs)
    generate_permutations(cur + '4', n, combs)

num_combs = len(n)
while True:
    combs = set()
    generate_permutations('', num_combs, combs)

    minor = float(inf)
    for comb in combs:
        if int(comb) >= int(n) and int(comb) < minor:
            minor = int(comb)
            
    if minor != float(inf):
        break
    num_combs += 1

print(minor)
