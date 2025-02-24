class Item:
    def __init__(self, id, weight, value):
        self.id, self.weight, self.value = id, weight, value
        
def knapsack(items, capacity):
    items.sort(key=lambda item: item.value/item.weight, reverse=True)
    current_bag = []
    current_weight = 0
    i = 0
    
    while current_weight < capacity and i < len(items):
        available = capacity - current_weight
        item_weight = items[i].weight
        
        if item_weight >= available:
            percent = available / item_weight
            item_weight = item_weight * percent
            
        current_weight += item_weight
        current_bag.append((items[i].id, item_weight))

        i += 1
    
    return current_bag


items = [
    Item('Notebook', 5, 4100),
    Item('Kindle', 1, 350),
    Item('Quadro', 4, 5000),
    Item('Livro', 3, 90),
    Item('Tablet', 3, 3500),
]

print(knapsack(items, 10))


# items = [
#     Item('Quadro', 4, 5000),    1250
#     Item('Tablet', 3, 3500),    1166
#     Item('Notebook', 5, 4100),  820
#     Item('Kindle', 1, 350),     350
#     Item('Livro', 3, 90),       30
# ]

