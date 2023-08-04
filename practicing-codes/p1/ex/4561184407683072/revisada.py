s1 = input()
s2 = input()

menor_len = len(s1) if len(s1) <= len(s2) else len(s2)

troca = False
for i in range(menor_len):
    if s1[i] == s2[i]:
        print(f"'{s1[i]}' coincidente na posição {i + 1}")
        troca = True

if troca:
    print('Senha não alterada')
if not troca:
    print('Senha alterada com sucesso')
