m = int(input())

if m <= 3:
    tx = 0.5*m
elif m > 3:
    if m >= 5:
        blocos = m // 5
        tx = 3*blocos + (m%5)*0.7
        
    else:
        tx = m*0.7

tot = 1 + tx

print(f'R$ {tot:.2f}')

