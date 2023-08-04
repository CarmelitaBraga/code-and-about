media_ssp = float(input())
lista = ""

while True:
    soma = 0 

    valores = input().split()

    if valores[0] == 'fim':
        break
    else:
        for valor in valores:
            soma += int(valor)
            media = soma/len(valores)
    
        if media > media_ssp:

            for i in range(len(valores)):
                if i == (len(valores)-1):
                    lista += valores[i] + '\n'
                else:
                    lista += valores[i] + ' ' 


        elif media < (media_ssp/2):
            break

print(lista, end='')
