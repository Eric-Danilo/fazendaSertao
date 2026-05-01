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