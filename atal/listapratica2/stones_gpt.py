def max_stones(a, b, c):
    # Priorizar a operação (b, c) primeiro
    op2 = min(b, c // 2)
    b -= op2  # Atualiza o valor de b depois de usar a operação
    stones = op2 * 3  # Cada operação dá 3 pedras

    # Depois, fazer a operação (a, b)
    op1 = min(a, b // 2)
    stones += op1 * 3  # Cada operação dá 3 pedras

    return stones

# Leitura da entrada
t = int(input())  # Número de casos de teste
for _ in range(t):
    a, b, c = map(int, input().split())
    print(max_stones(a, b, c))
