u1 = int(input())
r1 = int(input())

u2 = int(input())
r2 = int(input())

u3 = int(input())
r3 = int(input())

i1 = (u1 / r1)
i2 = (u2 / r2)
i3 = (u3 / r3)

if i1 > i2 and i1 > i3 or i1 == i2 and i1 > i3:
    print('condutor com maior corrente: 1')
    if i1 < 0.001:
        print(f'maior corrente: {i1*1000000:.2f} µA')
    elif i1 < 1:
        print(f'maior corrente: {i1*1000:.2f} mA')
    elif i1 >= 1:
        print(f'maior corrente: {i1:.2f} A')
elif i2 > i1 and i2 > i3 or i2 == i3 and i2 > i1:
    print('condutor com maior corrente: 2')
    if i2 < 0.001:
        print(f'maior corrente: {i2*1000000:.2f} µA')
    elif i2 < 1:
        print(f'maior corrente: {i2*1000:.2f} mA')
    elif i2 >= 1:
        print(f'maior corrente: {i2:.2f} A')
elif i3 > i2 and i3 > i1:
    print('condutor com maior corrente: 3')
    if i3 < 0.001:
        print(f'maior corrente: {i3*1000000:.2f} µA')
    elif i3 < 1:
        print(f'maior corrente: {i3*1000:.2f} mA')
    elif i3 >= 1:
        print(f'maior corrente: {i3:.2f} A')


