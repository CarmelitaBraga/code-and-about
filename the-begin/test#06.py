nome = input('Qual é o seu nome?')
print('Prazer em te conhecer, {:=^20}!'.format(nome))

n1 = int(input('Um valor:'))
n2 = int(input('Outro valor:'))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('A soma vale: {}. \n A multiplicação vale: {}. \n A divisão vale: {:.3f}.'.format(s, m, d), end='')
print('A divisão inteira vale: {}. \n A exponenciação vale: {}.'.format(di, e))
