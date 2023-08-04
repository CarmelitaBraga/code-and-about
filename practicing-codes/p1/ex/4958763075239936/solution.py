seq = input().split()
pos = 0

for i in range(len(seq)):
    if len(seq) == 1: break
    elif i == len(seq)-1:
        if seq[-1] < seq[-2]:
            pos = len(seq)
    else:
        if seq[i] > seq[i+1]:
            pos = i + 1
            break

if pos > 0:
    print(f'fora de ordem: {pos+1}')
else:
    print('em ordem')

