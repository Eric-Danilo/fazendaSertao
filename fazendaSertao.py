cliente = []
administrador = []
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
        
        for cli in cliente:
            if cli[0] == nome_usuario and cli[1] == senha_usuario:
                print('Login realizado como CLIENTE!')
                logado = True
        
        if logado == False:
            print('Usuario ou senha incorretos!')

    elif opcao == 2:
        print('Voce e ADM ou CLIENTE?')
        tipo_usuario = int(input('Digite 1- ADM ou 2- CLIENTE: '))

        if tipo_usuario == 1:
            print('----Cadastro ADM---------')
        elif tipo_usuario == 2:
            print('----Cadastro CLIENTE-----')
    elif opcao == 3:
        print('Saindo do sistema.......')
        break