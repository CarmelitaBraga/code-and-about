while True:
    a = int(input('a? '))
    b = int(input('b? '))
    c = int(input('c? '))

    delta = (b**2)-(4*a*c)
    if a != 0 and delta > 0:
        break

    print('equação inválida: tente novamente')


x1 = ((-b)+(delta**(1/2)))/(2*a)
x2 = ((-b)-(delta**(1/2)))/(2*a)

print(f'{x1:.3f}')
print(f'{x2:.3f}')


'''while True:
    a = int(input("a? "))
    b = int(input("b? "))
    c = int(input("c? "))
    delta = (b**2) - 4*a*c
    if delta <= 0: 
        print("equação inválida: tente novamente")
    else:
        raiz1 = ((-b) + (delta**(1/2))) / (2*a)
        raiz2 = ((-b) - (delta**(1/2))) / (2*a)
        print(f"{raiz1:.3f}\n{raiz2:.3f}")
        break'''
