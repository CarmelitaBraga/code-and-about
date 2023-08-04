'''tempo = int(input('Quantos anos tem seu carro? '))
if tempo<=3:
    print('Carro novo!')
else:
    print('Carro velho!')
print('--FIM--')'''

'''tempo = int(input('Quantos anos tem seu carro? '))
print('Carro novinho!' if tempo<=3 else 'Carro usado!')'''

'''nome = str(input('Qual é o seu nome? '))
if nome == 'Taylor':
    print('Que nome lindo! Sabia que você é especial, {}?'.format(nome))
else:
    print('Tenha um bom dia, {}.'.format(nome))'''

n1 = float(input('A primeira nota: '))
n2 = float(input('A segunda nota: '))
m = (n1 + n2)/2
if m>=7:
    print('Parabéns, você foi aprovado!')
else:
    print('Nota insuficiente, você está de recuperação!')
print('Sua nota final: {:.1f}.'.format(m))





