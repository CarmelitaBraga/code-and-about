total = 0
vezes = 0

while True:
    x, y = str(input()).split()
    x = float(x)
    y = float(y)
    dis = ((x-0)**2 + (y-0)**2)**(1/2)
    
    if dis > 200: break

    total += dis
    vezes += 1

    print(f'{dis:.2f}cm')

media = total/vezes
print('--')
print(f'num disparos: {vezes}')
print(f'distancia media: {media:.2f}cm')

    
