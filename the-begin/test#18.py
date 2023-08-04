guys = list()
dados = list()
totmai = totmen = 0          #a igualdade só funcionará para variáveis simples
for r in range(0, 4):
    dados.append(str(input('Nome: ')))
    dados.append(int(input('Idade: ')))
    guys.append(dados[:])
    dados.clear()
for x in guys:
    if x[1] >= 21:
        print(f'{x[0]} é maior de idade.')
        totmai += 1
    else:
        print(f'{x[0]} é menor de idade.')
        totmen += 1
print(f'{guys}')
print(f'{totmai} pessoas são maiores de idade.'
      f'\n{totmen} pessoas são menores de idade.') 


'''gal = [['Nicolas', 22], ['Carmelita', 21], ['Joaquim', 25], ['Gabriel', 21]]
print(gal[0][0])
print(gal[1][0])
print(gal[2][1])
for p in gal:
    print(p[0])      #tentar dar nome ao zero e o um dos conjuntos
    print(f'{p[0]} tem {p[1]} anos de idade.')'''


'''teste = list()
teste.append('Gustavo')
teste.append(40)
galera = list()
galera.append(teste[:])
teste[0] = 'Mary'
teste[1] = 22
print(f'{teste}')
print(f'{galera}')'''







'''EXERCICIOS COPIA E COLA (APENAS INSPIRAÇÃO)


[DESAFIO 088]
Demorei um pouquinho para resolver kk

from random import randint
from time import sleep

lista = list()
gerados = list()
print('-'*50)
print(f'{"MEGA SENA":^50}')
print('-'*50)
num = int(input('Quantos jogos deseja gerar:'))
print('='*50)
for i in range(num):
    for j in range(0, 6):
        gerar = randint(1, 8)
        if gerar in lista:
            while gerar in lista:
                gerar = randint(1, 60)
                if gerar not in lista:
                     lista.append(gerar)
                     break
        else:
            lista.append(gerar)
    gerados.append(lista[:])
    lista.clear()
    sleep(1)
    print(f'Jogo {i+1}: {gerados[i]}')
print('-'*50)
print(f'{"BOA SORTE":^50}')
print('-'*50)


[DESAFIO 089]

lista = list()
notas = list()
nomes = list()

while True:
    nome = str(input('Nome do aluno:').capitalize())
    nomes.append(nome)
    nt1 = float(input('Nota 1:'))
    notas.append(nt1)
    nt2 = float(input('Nota 2:'))
    notas.append(nt2)

    nomes.append(notas[:])
    lista.append(nomes[:])
    notas.clear()
    nomes.clear()
    opcao = str(input('Deseja continuar[s/n]:'))
    print('=' * 60)

    if opcao in 'sS':
        continue
    elif opcao in 'nN':
        break
tamanho = len(lista)
guarda = tamanho * 2
print('Nº  NOME              MÉDIA')
print('-'*40)

for i in range(tamanho):
    print(f'{i+1}   {lista[i][0]:<18}', end='')
    media = 0
    for j in range(2):
        media += lista[i][1][j]
    media = media / 2
    print(f'{media:.1f}')
print('-'*50)
while True:
    number = int(input('Mostrar nota de qual aluno (negativo!):'))
    if number < 0:
        break
    else:
        print(f'As notas de {lista[number - 1][0]} são: {lista[number - 1][1]}')
        print('=' * 60)
'''