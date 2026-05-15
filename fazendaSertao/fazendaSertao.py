administrador = [['eric', '123']]
cliente = [['cire','123']]
rebanho = []
estoque = []
producao = []
logado = False

while True:
    print('-----Sistema Gestao Agropecuaria-----')
    print('1. Login')
    print('2. Cadastro usuario')
    print('3. Sair')
    print('-------------------------------------')
    opcao_menu = int(input('Digite a opcao que deseja: '))

    if opcao_menu == 1:
        nome_usuario = input('Insira seu nome de usuario: ')
        senha_usuario = input('Insira sua senha: ')
        logado = False

        for adm in administrador:
            if adm[0] == nome_usuario and adm[1] == senha_usuario:
                print('Login realizado como ADM!')
                logado = True
                tipo_login = 'ADM'
                break

        if logado and tipo_login == 'ADM':
            while True:
                print('----MENU ADMINISTRADOR----')
                print('1. Cadastrar animal')
                print('2. Listar animais')
                print('3. Buscar animal')
                print('4. Atualizar animal')
                print('5. Remover animal')
                print('6. Adicionar produtos')
                print('7. Voltar')

                opcao_adm = int(input('Escolha a opção: '))

                if opcao_adm == 1:
                    tipo = input('Tipos do animal: ')
                    iden_animal = input('Identificação do animal: ')
                    status_animal = input('Status do animal: ')

                    rebanho.append([tipo, iden_animal, status_animal])
                    print('Animal cadastrado com sucesso!')

                elif opcao_adm == 2:
                    if len(rebanho) <= 0:
                        print('Nenhum animal cadastrado!')
                    else:
                        for animal in rebanho:
                            print(f'Tipo: {animal[0]} - Identificação: {animal[1]} - Status: {animal[2]}')
                    
                elif opcao_adm == 3:
                    buscar_animal = input('Insira o número do animal que você busca: ')
                    encontrou = False                      
                        
                    for animal in rebanho:
                        if animal[1] == buscar_animal:
                            print(f'Tipo: {animal[0]} - Identificação: {animal[1]} - Status: {animal[2]}')
                            encontrou = True

                    if encontrou == False:
                        print('Animal não encontrado ou não foi cadastrado!')

                elif opcao_adm == 4:                           
                    print('Qual animal você deseja atualizar?')
                    atualize_animal = input("Insira o ID do animal a ser alterado: ")

                    for animal in rebanho:
                        if animal[1] == atualize_animal:
                            anim_atualizar = input('Novo animal: ')
                            status_atualizar = input('Novo status: ')  

                            animal[0] = anim_atualizar
                            animal[2] = status_atualizar
                            print('Atualizado com sucesso!')

                elif opcao_adm == 5:
                    print('Qual animal você quer remover?')
                    remove_animal = input('Digite o ID do animal: ')
                    item = 0

                    for animal in rebanho:
                        if animal[1] == remove_animal:
                            rebanho.pop(item)
                            print('Animal removido!')
                            break
                        item += 1
                    else:
                        print("Animal não encontrado!")

                elif opcao_adm == 6:
                    while True:
                        print('----PRODUÇÃO / ESTOQUE----')
                        print('1. Registrar o produto produzido')
                        print('2. Adicionar o derivado no estoque')
                        print('3. Voltar')

                        opcao_produto = int(input('Escolha a opção: '))

                        if opcao_produto == 1:
                            n_produto = input('Nome do produzido: ')
                            quan_produto = float(input('Quantidade que foi produzido: '))

                            producao.append([n_produto, quan_produto])
                            print('Produzido resgistrado!')

                        elif opcao_produto == 2:
                            add_produ = input('Insira o produto produzido: ')
                            peso_produ = float(input('Peso do produto: '))
                            val_venda = float(input('Valor de venda em R$: '))
                            
                            estoque.append([add_produ, peso_produ, val_venda])
                            print('O produto foi adicionado no estoque!')

                        elif opcao_produto == 3:
                            print('Voltando para o menu de ADM...')
                            break
                        else:
                            print('Opção inválida!')

                elif opcao_adm == 7:
                    break

        for cli in cliente:
            if cli[0] == nome_usuario and cli[1] == senha_usuario:
                print('Login realizado como CLIENTE!')
                logado = True
                tipo_login = 'CLIENTE'
                break

        if logado and tipo_login == 'CLIENTE':
            while True:
                print('---- MENU CLIENTE ----')
                print('1. Olhar produtos')
                print('2. Comprar')
                print('3. Voltar')
                print('----------------------')

                opcao_cli = int(input('Escolha a opção: '))
                if opcao_cli == 1:
                    produtos_venda = []
                    for prod in estoque:                        
                        produtos_venda.append(prod)
                        print(produtos_venda)
                    print('to aq')

                elif opcao_cli == 2:
                    print('compra')
                elif opcao_cli == 3:
                    break


        if logado == False:
            print('Usuario ou senha incorretos!')

    elif opcao_menu == 2:
        print('Voce e ADM ou CLIENTE?')
        tipo_usuario = int(input('Digite 1- ADM ou 2- CLIENTE: '))

        if tipo_usuario == 1:
            print('----Cadastro ADM----')
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

    elif opcao_menu == 3:
        print('Saindo do sistema...')
        break