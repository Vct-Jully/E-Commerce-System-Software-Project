# Variáveis para armazenar um único usuário e senha
usuario = None
senha = None
logado = False  # Controle de login

# Lista de produtos
produtos = [
    {"nome": "Notebook", "preco": 3500},
    {"nome": "Smartphone", "preco": 2000},
    {"nome": "Tênis", "preco": 300}
]

def exibir_produtos():
    """Exibe a lista de produtos disponíveis"""
    print("\nLista de Produtos Disponíveis:")
    for p in produtos:
        print(f"Nome: {p['nome']}, Preço: R${p['preco']}")

while True:
    print("\n=== Menu ===")
    print("1 - Cadastrar Usuário")
    print("2 - Fazer Login")
    print("3 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        # Cadastro
        usuario = input("Cadastre um nome de usuário: ")
        senha = input("Cadastre uma senha: ")
        print("Usuário cadastrado com sucesso!\n")

    elif opcao == "2":
        # Login
        if usuario is None:
            print("Nenhum usuário cadastrado. Cadastre-se primeiro!")
            continue

        user_input = input("Digite seu usuário: ")
        senha_input = input("Digite sua senha: ")

        if user_input == usuario and senha_input == senha:
            print("Login bem-sucedido!")
            logado = True  # Marca que o usuário está logado

            # Após login, exibir menu para ver produtos
            while logado:
                print("\n=== Menu do Usuário ===")
                print("1 - Ver Produtos")
                print("2 - Logout")

                opcao_user = input("Escolha uma opção: ")

                if opcao_user == "1":
                    exibir_produtos()
                elif opcao_user == "2":
                    print("Você saiu da conta.")
                    logado = False  # Sai do loop e retorna ao menu principal
                else:
                    print("Opção inválida! Escolha 1 ou 2.")

        else:
            print("Usuário ou senha incorretos.")

    elif opcao == "3":
        print("Saindo...")
        break

    else:
        print("Opção inválida! Escolha 1, 2 ou 3.")
