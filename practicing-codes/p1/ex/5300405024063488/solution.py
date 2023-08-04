price = float(input('Digite o preço da unidade do tijolo (Em reais): '))
tij_altura = float(input('Digite a altura do tijolo (Em metros): '))
tij_largura = float(input('Digite o comprimento do tijolo (Em metros): '))
par_altura = float(input('Digite a altura das paredes (Em metros): '))
par_largura = float(input('Digite o comprimento das paredes (Em metros): '))

num_tijolos_altura = par_altura / tij_altura
num_tijolos_largura = par_largura / tij_largura
num_tijolos_total = num_tijolos_altura * num_tijolos_largura
tijolos_price = price * num_tijolos_total


print(f'O número total de tijolos é {num_tijolos_total:.1f} e o orçamento final é de R$ {tijolos_price:.1f}')

