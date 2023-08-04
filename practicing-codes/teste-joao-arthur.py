#lista = list(range(200, 600, 5))
lista = list(range(0, 500, 5))
for _ in lista:
    print(_%100) #%95)


# terminal: python3  teste.py | sort | uniq -c | sort -nk 2
