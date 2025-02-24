n = int(input())
list_cidades = []

for _ in range(n):
    a, c = input().split()
    list_cidades.append((a, c))
    
sum_total = 0
for i in range(len(list_cidades)):
    aj, cj = list_cidades[i]
    ai, _ = list_cidades[i-1]
    calc = int(ai)-int(aj)
    
    print(calc)
    sum_total += max(int(cj), calc)
    
print(sum_total)
                



menos_paradas(lista_distancia_postos, capacidade_k):
    paradas_finais = []
    ultima_dist = 0
    for each d in lista_distancia_postos
        if (d-ultima_dist) / capacidade_k > 1:
            paradas_finais.append(i)
            ultima_dist = d
            
