sinal = -1
pi = 4
den = 1
velho_pi = 0

num = float(input())

while True:
    print(f'{pi:.6f}')

    if abs(pi - velho_pi) < num: break

    velho_pi = pi
    den += 2
    sinal *= -1
    pi -= 4*(sinal * (1/den))

    
    
