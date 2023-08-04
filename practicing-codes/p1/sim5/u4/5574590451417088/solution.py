N = int(input())
dobr = ''
n_dob = ''
num_dob = 0
num_nor = 0

for vzs in range(N):
    p = str(input())
    
    # pega palavra e checa letras
    soma = 0
    for i in range(len(p)):
        if i < len(p)-1:
            if p[i] == p[i+1]:
                soma += 1

    if soma > 0:
        dobr += p + '\n'
        num_dob += 1
    else:
        n_dob += p + '\n'
        num_nor += 1


print(f'{num_dob} palavra(s) com letras dobradas:')
print(dobr, end='')

print('---')

print(f'{num_nor} palavra(s) sem letras dobradas:')
print(n_dob, end='')
