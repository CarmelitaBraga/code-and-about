# n = int(input())
# factor = 1

# while factor * factor <= n:
#     if n % factor == 0:
#         print(factor)
#         if factor != n // factor and n // factor != n:  # Avoid printing the same factor twice
#             print(n // factor)
#     factor += 1


# print(n)


n = int(input())
small_factors = []
large_factors = []

factor = 1
while factor * factor <= n:
    if n % factor == 0:
        small_factors.append(factor)
        if factor != n // factor:
            large_factors.append(n // factor)
    factor += 1

for f in small_factors:
    print(f)
for f in reversed(large_factors):
    print(f)


# n = int(input())
# factor = 1

# while factor <= n:
#     if n % factor == 0:
#         print(factor)
#     factor += 1
    