# Lista de administradores cadastrados diretamente no código
admins = [
    {"user": "admin", "password": "admin123"},
    {"user": "gestor", "password": "gestor123"}
]

users = []

# Variáveis para usuário comum
user = None
password = None
logged = False  # Controle de login
is_admin = False  # Determina se o usuário logado é administrador

# Lista de produtos
products = [
    {"nome": "Notebook", "preco": 3500},
    {"nome": "Smartphone", "preco": 2000},
    {"nome": "Tênis", "preco": 300}
]

# Carrinho de compras
cart = []

def show_products():
    """Exibe a lista de produtos disponíveis com um índice"""
    print("\nLista de Produtos Disponíveis:")
    for i, p in enumerate(products, start=1):
        print(f"{i} - Nome: {p['nome']}, Preço: R${p['preco']}")

def buy_or_add_to_cart():
    """Permite ao usuário escolher um produto para comprar ou adicionar ao carrinho"""
    show_products()

    try:
        choice = int(input("\nDigite o número do produto desejado: ")) - 1
        
        if 0 <= choice < len(products):
            print("\n1 - Adicionar ao carrinho")
            print("2 - Comprar agora")
            action = input("Escolha uma opção: ")

            if action == "1":
                cart.append(products[choice])
                print(f"\n{products[choice]['nome']} foi adicionado ao carrinho!\n")
            elif action == "2":
                print(f"\nVocê comprou: {products[choice]['nome']} por R${products[choice]['preco']}!\n")
            else:
                print("\nOpção inválida! Escolha 1 ou 2.\n")

        else:
            print("\nOpção inválida! Escolha um número da lista.\n")
    
    except ValueError:
        print("\nEntrada inválida! Digite um número.\n")

def view_cart():
    """Exibe os itens no carrinho e permite ações"""
    if not cart:
        print("\nSeu carrinho está vazio!\n")
        return

    print("\n=== Carrinho de Compras ===")
    total = 0
    for i, item in enumerate(cart, start=1):
        print(f"{i} - {item['nome']} | R${item['preco']}")
        total += item['preco']
    
    print(f"\nTotal da compra: R${total}")

    while True:
        print("\n1 - Comprar um item")
        print("2 - Comprar todos os itens")
        print("3 - Remover um item")
        print("4 - Esvaziar carrinho")
        print("5 - Voltar ao menu")

        action = input("Escolha uma opção: ")

        if action == "1":
            try:
                item_index = int(input("\nDigite o número do item que deseja comprar: ")) - 1
                if 0 <= item_index < len(cart):
                    print("1 - Cartão de crédito")
                    print("2 - Pix")
                    print("3 - Boleto bancário")

                    payment_method = int(input("Selecione a forma de pagamento: "))

                    if payment_method not in [1, 2, 3]:
                        print("\nForma de pagamento inválida")
                        continue

                    item = cart.pop(item_index)
                    print(f"\nVocê comprou: {item['nome']} por R${item['preco']} utilizando {'Cartão' if payment_method == 1 else 'Pix' if payment_method == 2 else 'Boleto'}!\n")
                else:
                    print("\nOpção inválida!\n")
            except ValueError:
                print("\nEntrada inválida! Digite um número.\n")

        elif action == "2":
            if cart:
                print("\nCompra finalizada! Você comprou:")
                for item in cart:
                    print(f"- {item['nome']} por R${item['preco']}")
                cart.clear()
                print("\nObrigado por comprar conosco!\n")
            else:
                print("\nSeu carrinho está vazio!\n")
            break

        elif action == "3":
            try:
                item_index = int(input("\nDigite o número do item que deseja remover: ")) - 1
                if 0 <= item_index < len(cart):
                    removed_item = cart.pop(item_index)
                    print(f"\n{removed_item['nome']} foi removido do carrinho.\n")
                else:
                    print("\nOpção inválida!\n")
            except ValueError:
                print("\nEntrada inválida! Digite um número.\n")

        elif action == "4":
            cart.clear()
            print("\nTodos os itens foram removidos do carrinho.\n")
            break

        elif action == "5":
            break

        else:
            print("\nOpção inválida! Escolha entre 1 e 5.\n")

def admin_menu():
    """Menu de administração para gerenciar produtos"""
    while True:
        print("\n=== Menu de Administração ===")
        print("1 - Adicionar Produto")
        print("2 - Editar Produto")
        print("3 - Remover Produto")
        print("4 - Voltar ao menu do usuário")

        action = input("Escolha uma opção: ")

        if action == "1":
            nome = input("\nDigite o nome do produto: ")
            preco = float(input("Digite o preço do produto: R$"))
            products.append({"nome": nome, "preco": preco})
            print(f"\nProduto {nome} adicionado ao inventário!\n")

        elif action == "2":
            try:
                show_products()
                index = int(input("\nDigite o número do produto a ser editado: ")) - 1
                if 0 <= index < len(products):
                    nome = input("Digite o novo nome do produto: ")
                    preco = float(input("Digite o novo preço do produto: R$"))
                    products[index] = {"nome": nome, "preco": preco}
                    print(f"\nProduto {nome} foi atualizado!\n")
                else:
                    print("\nProduto não encontrado!\n")
            except ValueError:
                print("\nEntrada inválida!\n")

        elif action == "3":
            try:
                show_products()
                index = int(input("\nDigite o número do produto a ser removido: ")) - 1
                if 0 <= index < len(products):
                    removed_product = products.pop(index)
                    print(f"\nProduto {removed_product['nome']} foi removido!\n")
                else:
                    print("\nProduto não encontrado!\n")
            except ValueError:
                print("\nEntrada inválida!\n")

        elif action == "4":
            break

        else:
            print("\nOpção inválida! Escolha entre 1 e 4.\n")

while True:
    print("\n=== Menu ===")
    print("1 - Fazer Login")
    print("2 - Cadastrar Usuário")
    print("3 - Sair")

    option = input("Escolha uma opção: ")

    if option == "1":
        user_input = input("Digite seu usuário: ")
        password_input = input("Digite sua senha: ")

        # Verifica se o usuário é um admin
        is_admin = any(admin["user"] == user_input and admin["password"] == password_input for admin in admins)

        if is_admin or (user_input == user and password_input == password):
            print("Login bem-sucedido!")
            logged = True

            while logged:
                print("\n=== Menu do Usuário ===")
                print("1 - Ver Produtos")
                print("2 - Comprar ou Adicionar ao Carrinho")
                print("3 - Ver Carrinho")
                if is_admin:
                    print("4 - Acessar Menu de Administração")
                print("5 - Logout")

                option_user = input("Escolha uma opção: ")

                if option_user == "1":
                    show_products()
                elif option_user == "2":
                    buy_or_add_to_cart()
                elif option_user == "3":
                    view_cart()
                elif option_user == "4" and is_admin:
                    admin_menu()
                elif option_user == "5":
                    print("Você saiu da conta.")
                    logged = False
                else:
                    print("Opção inválida! Escolha entre 1 e 5.")

        elif user_input == user and password_input == password:
            print("Login realizado com sucesso!")
            logged = True

            while logged:
                print("\n=== Menu do Usuário ===")
                print("1 - Ver Produtos")
                print("2 - Comprar ou Adicionar ao Carrinho")
                print("3 - Ver Carrinho")
                print("4 - Logout")

                option_user = input("Selecione uma opção: ")

                if option_user == "1":
                    show_products()
                elif option_user == "2":
                    buy_or_add_to_cart()
                elif option_user == "3":
                    view_cart()
                elif option_user == "4":
                    print("Você saiu da conta.")
                    logged = False
                else:
                    print("Opção inválida! Escolha entre 1 e 4.")

        else:
            print("Usuário ou senha incorretos.")

    elif option == "2":
        user = input("Cadastre um nome de usuário: ")
        password = input("Cadastre uma senha: ")
        print("Usuário cadastrado com sucesso!\n")

    elif option == "3":
        print("Saindo...")
        break

    else:
        print("Opção inválida! Escolha 1, 2 ou 3.")
