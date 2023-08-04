'''senha_atual = input()
senha_nova = input()

menor_tamanho = len(senha_atual) if len(senha_atual) <= len(senha_nova) else len(senha_nova)

pos, letra = [], []

for i in range(menor_tamanho):
    if senha_atual[i] == senha_nova[i]:
        pos.append(i)
        letra.append(senha_atual[i])

if len(pos) > 0:
    for j in range(len(pos)):
        print(f"'{letra[j]}' coincidente na posição {pos[j] + 1}")
    print('Senha não alterada')
else:
    print('Senha alterada com sucesso')
'''

s1 = input()
s2 = input()

menor_len = len(s1) if len(s1) <= len(s2) else len(s2)

for i in range(menor_len):
    if s1[i] == s2[i]:
        print(f"'{s1[i]}")

































