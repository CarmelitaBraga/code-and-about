lista_clientes = []
final = []

while True:
    option = input()
    usuario = False

    if option == 'finalizar': break
    
    elif option == 'cadastrar':
        cpf = input()
        nome = input()
        posto = input()
        for e in lista_clientes:
            if e[0] == cpf:
                usuario = True
        if not usuario:
            pontos = 300
            lista_clientes.append([cpf, nome, posto, pontos])
            final.append('Usuário cadastrado com sucesso.')
        else: final.append('Usuário já existente.')

    elif option == 'atualizar':
        cpf = input()
        posto = input()
        for e in lista_clientes:
            if e[0] == cpf:
                usuario = True
                if e[2] == posto:
                    e[3] += 200
                else:
                    e[3] += 100
        if usuario: final.append('Usuário atualizado com sucesso.')
        else: final.append('Usuário inexistente.')

    elif option == 'consultar':
        cpf = input()
        for e in lista_clientes:
            if e[0] == cpf:
                final.append(f'Nome: {e[1]}')
                final.append(f'CPF: {e[0]}')
                final.append(f'Saldo: {e[3]:.2f}')
                usuario = True
        if not usuario:
            print('Usuário inexistente.')

for elementos in final:
    print(elementos)
