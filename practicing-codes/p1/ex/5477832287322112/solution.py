msg = str(input())
cod = str(input())

sen = ''

for i in range(len(msg)):
    if msg[i] == str(i):
        sen += cod[i]
    else:
        sen += msg[i]

print(sen)
