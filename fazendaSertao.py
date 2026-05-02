cliente = []
administrador = [['eric','123']]
rebanho = []
logado = False

while True:
    print('-----Sistema Gestao Agropecuaria------')
    print('1. Login')
    print('2. Cadastro usuario')
    print('3. Sair')
    print('--------------------------------------')
    opcao = int(input('Digite a opcao que deseja: '))

    if opcao == 1:
        nome_usuario = input('Insira seu nome de usuario: ')
        senha_usuario = input('Insira sua senha: ')
        logado = False

        for adm in administrador:
            if adm[0] == nome_usuario and adm[1] == senha_usuario:
                print('Login realizado como ADM!')
                logado = True
                tipo_login = 'ADM'

                if logado and tipo_login == 'ADM':
                    while True:
                        print('-----MENU ADMINISTRADOR-----')
                        print('1. Cadastrar animal')
                        print('2. Listar animais')
                        print('3. Buscar animal')
                        print('4. Atualizar animal')
                        print('5. Remover animal')
                        print('6. Voltar')

                        opcao = int(input('Escolha a opção: '))

                        if opcao == 1:
                            tipo = input('Tipos (Bovino, Caprino, Ovino, Suino): ')
                            iden_animal = input('Identificação do animal: ')
                            status_animal = input('Status: ')

                            rebanho.append([tipo, iden_animal, status_animal])
                            print('Animal cadastrado com sucesso!')

                        elif opcao == 2:
                            if len(rebanho) <= 0:
                                print('Nenhum animal cadastrado!')
                            else:
                                for animal in rebanho:
                                    print(f'Tipo: {animal[0]} | ID: {animal[1]} | Status: {animal[2]}')
                        
                        elif opcao == 3:
                            buscar_animal = input('Insira o ID do animal que você busca: ')
                            encontrou = False                      
                            
                            for animal in rebanho:
                                if animal[1] == buscar_animal:
                                    print(f'Animal encontrado: {animal}')
                                    encontrou = True
                                else:
                                    print('Animal não encontrado/cadastrado!')

                        elif opcao == 4:                           
                            print('Qual animal você deseja alterar/atualizar?')
                            atualize_animal = input("Insira o ID do animal a ser alterado: ")

                            for animal in rebanho:
                                if animal[1] == atualize_animal:
                                    anim_atualizar = input('Novo animal: ')
                                    status_atualizar = input('Novo status: ')  

                                    animal[0] = anim_atualizar
                                    animal[2] = status_atualizar
                                    print('Atualizado com sucesso!')

                        elif opcao == 5:
                            print('Qual animal você quer remover?')
                            remove_animal = input('Digite o ID do animal: ')
                            item = 0

                            for animal in rebanho:
                                if animal[1] == remove_animal:
                                    rebanho.pop(item)
                                    print('Animal removido')
                                    break
                                item += 1
                            else:
                                print("Animal não encontrado!")

                        elif opcao == 6:
                            break

        for cli in cliente:
            if cli[0] == nome_usuario and cli[1] == senha_usuario:
                print('Login realizado como CLIENTE!')
                logado = True
                tipo_login = 'CLIENTE'
        
        if logado == False:
            print('Usuario ou senha incorretos!')

    elif opcao == 2:
        print('Voce e ADM ou CLIENTE?')
        tipo_usuario = int(input('Digite 1- ADM ou 2- CLIENTE: '))

        if tipo_usuario == 1:
            print('----Cadastro ADM---------')
            nome_usuario = input("Insira o nome do usuario: ")
            senha_usuario = input("Crie sua senha: ")
            administrador.append([nome_usuario, senha_usuario])
            print('ADM - Cadastrado com sucesso!!!')

        elif tipo_usuario == 2:
            print('----Cadastro CLIENTE-----')
            nome_usuario = input("Insira o nome do usuario: ")
            senha_usuario = input("Crie sua senha: ")
            cliente.append([nome_usuario, senha_usuario])
            print('CLIENTE - Cadastrado com sucesso!!!')

    elif opcao == 3:
        print('Saindo do sistema.......')
        break