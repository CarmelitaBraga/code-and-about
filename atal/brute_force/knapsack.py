class Item:
    def __init__(self, id, peso, valor):
        self.id, self.peso, self.valor = id, peso, valor


def knapsack(itens, max_w):
    n = len(itens)
    
    def generate_permutations(cur, n, combs):
        if len(cur) == n:
            combs.add(cur)
            return

        generate_permutations(cur + '0', n, combs)
        generate_permutations(cur + '1', n, combs)

    combs = set()
    generate_permutations('', n, combs)
    
    max_value = 0
    for c in combs:
        comb_value = 0
        comb_weight = 0
        for i in range(n):
            if int(c[i]) > 0 and (comb_weight + itens[i].peso) <= max_w:
                comb_weight += itens[i].peso
                comb_value += itens[i].valor

        if comb_value > max_value:
            max_value = comb_value
                
    return max_value


itens = [
    Item('notebook', 7, 4500),
    Item('livro', 2, 60),
    Item('carregador', 1, 50),
    Item('tablet', 4, 3700),
    Item('blusa', 1, 90),
]

w = 10
print(knapsack(itens, w))