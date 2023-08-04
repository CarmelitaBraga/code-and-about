sequencia = input().split()

i = 0
ordem = True
while True:
    if (i + 1) == len(sequencia): break

    i += 1
    if sequencia[i - 1] > sequencia[i]:
        print(f'fora de ordem: {i + 1}')
        ordem = False
        break

if ordem: print('em ordem')
