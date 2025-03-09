class Item:
    def __init__(self, id, peso, valor):
        self.id, self.peso, self.valor = id, peso, valor


def knapsack(itens, max_w):
    n = len(itens)
    max_value = 0
    
    def backtrack(index, current_weight, current_value):
        nonlocal max_value
        
        if index == n:
            max_value = max(max_value, current_value)
            return
        
        backtrack(index+1, current_weight, current_value)
        
        if itens[index].peso + current_weight <= max_w:
            backtrack(index + 1,
                      current_weight + itens[index].peso,
                      current_value + itens[index].valor)
        
    backtrack(0, 0, 0)
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