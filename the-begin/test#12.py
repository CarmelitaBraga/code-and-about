nome = str(input('Qual é o seu nome? '))
if nome == 'Carmelita':
    print('Que nome lindo!')
elif nome in 'Ana José Pedro Maria João':
    print('Seu nome é bem popular.')
else:
    print('Seu nome é interessante.')
print('Tenha um bom dia, {}!'.format(nome))