from math import ceil

def prioritario(idade):
    return idade <= 9 or idade >= 80

def divide_grupo(lista_idades):
    comum, prioridade = 0, 0
    for i in lista_idades:
        i = int(i)
        if prioritario(i):
            prioridade += 1
        else:
            comum += 1
    return comum, prioridade

def dias_de_vacinacao(n, d, idades):
    idades.sort(reverse=True)

    comum, prioridade = divide_grupo(idades)
    
    dias_risco = ceil(prioridade / int(d))
    dias_comuns = ceil(comum / int(d))
    
    return dias_risco + dias_comuns


t = int(input())
res = ''
for _ in range(t):
    n, d = input().split()
    idades = input().split()
    res += str(dias_de_vacinacao(n, d, idades)) + '\n'

print(res.strip())