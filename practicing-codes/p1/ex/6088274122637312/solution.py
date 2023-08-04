info = input().split()

nome = info[0]
string = f'{info[1]+info[2]+info[3]}'

for i in range(0, len(info), 4):
    if (info[i + 1] + info[i + 2] + info[i + 3]) < string:
        nome = info[i]
        string = (info[i + 1] + info[i + 2] + info[i + 3])

print(nome)

