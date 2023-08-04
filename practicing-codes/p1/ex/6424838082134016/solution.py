price = 99999999   #como fazer diferente?
hp = ''
area = 0
ha = ''
comfort = 0
hc = ''

while True:
    dados = input().split(',')
    
    if dados[0] == '---': break
    else:
        if float(dados[0]) < price:
            hp = dados[3]
            price = float(dados[0])
        if int(dados[1]) > area:
            ha = dados[3]
            area = int(dados[1])
        if int(dados[2]) > comfort:
            hc = dados[3]
            comfort = int(dados[2])

while True:
    crit = input()
    
    if crit == 'valor':
        print(hp)
    elif crit == 'tamanho':
        print(ha)
    elif crit == 'conforto':
        print(hc)

    if crit == 'fim': break
