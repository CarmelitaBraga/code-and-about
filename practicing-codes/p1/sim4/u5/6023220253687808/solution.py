num = int(input())
num1 = num // 10
num2 = num % 10
print(num1)
print(num2)

prox = num1 + num2
print(prox)

while True:
    num1 = num2
    num2 = prox
    prox = num2 + num1
    if prox > num: 
        print('---')
        print(f'{num} não é um repfigit.')
        break
    print(prox)
    if prox == num:
        print('---')
        print(f'{num} é um repfigit.')
        break

