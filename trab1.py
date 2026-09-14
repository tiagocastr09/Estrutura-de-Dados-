#login123

usuarios = {}

usuario_dig = input("Digite o ID: ")
senha_dig = int(input("Digite a senha: "))

if usuario_dig == "admin" and senha_dig == 12345:
    print("Bem Vindo")
else:
    print("Tente novamente. Login ou senha inválidos.")

while True:
    print("====================MENU====================\n")

    print("OPÇÕES\n")
    print("1- CADASTRAR USUÁRIO")
    print("2- LISTAR USUÁRIOS")
    print("3- REMOVER USUÁRIO")
    print("4- SAIR")

    opcao = int(input("Digite a opção desejada: "))
    if opcao == 1:
        nome = input("Digite o nome do usuário: ")
        senha = int(input("Digite a senha do usuário: "))
        usuarios[nome] = {"login": nome, "senha": senha}
        print(f"Usuário {nome} cadastrado com sucesso!")

    elif opcao == 2:
            if usuarios:
                print("Lista de usuários já cadastrados:")
                for nome, dados in usuarios.items():
                    print(f"Nome: {nome}, Senha: {dados['senha']}")
            else:
                print("Nenhum usuário foi cadastrado ainda.")

    elif opcao == 3:
        nome = input("Digite o nome do usuário que você deseja remover: ")
        if nome in usuarios:
            del usuarios[nome]
            print(f"Usuário {nome} removido com sucesso!")
        else:
            print(f"Usuário {nome} não encontrado.")    
    elif opcao == 4:
        print("Saindo do programa...")
        break