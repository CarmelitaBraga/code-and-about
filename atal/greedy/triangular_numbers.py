# n = int(input())

# counter = 0

# while True:
#     calc = (counter*(counter + 1)) / 2
#     if calc == n:
#         print("YES")
#         break
#     elif calc != n and calc < n:
#         counter += 1
#     else:
#         print("NO")
#         break

import math

def is_triangular(n):
    x = 1 + 8 * n
    sqrt_x = int(math.sqrt(x))
    
    if sqrt_x * sqrt_x == x:  # Check if 1 + 8n is a perfect square
        k = (-1 + sqrt_x) // 2
        if k * (k + 1) // 2 == n:  # Ensure k is valid
            return "YES"
    
    return "NO"

# Read input
n = int(input())
print(is_triangular(n))




# # TODO: estratégia com busca linear
# def linear_search(x, minor, maxi):
#     min_t = (minor*(minor+1)) / 2
#     max_t = (maxi*(maxi+1)) / 2
    
#     if min_t < 
    