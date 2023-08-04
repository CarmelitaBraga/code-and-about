a = int(input())
b = int(input())
c = int(input())

soma = a + b + c

if abs(b-c) < a < b+c:
    print(f'triangulo valido. {soma}')
elif abs(a-c) < b < a+c:
    print(f'triangulo valido. {soma}')
elif abs(a-b) < c < a+b:
    print(f'triangulo valido. {soma}')
else:
     print('triangulo invalido.')

