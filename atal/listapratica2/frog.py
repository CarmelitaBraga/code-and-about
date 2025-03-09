from math import inf

def custo_minimo(alturas):    
    def backtrack(alturas, i, custo):
        if i >= len(alturas):
            return custo
        
        c1 = backtrack(alturas, i+1, custo + abs(alturas[i-1] - alturas[i]))
        
        c2 = float(inf)
        if i < len(alturas)-1:
            c2 = backtrack(alturas, i+2, custo + abs(alturas[i-1] - alturas[i+1]))
        
        return min(c1, c2)

    custo_min = backtrack(alturas, 1, 0)
    return custo_min

num = int(input())
alturas = input().split()
alturas = [int(_) for _ in alturas]
print(custo_minimo(alturas))
