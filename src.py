# Variáveis para armazenar um único usuário e senha
user = None
password = None
logged = False  # Controle de login

# Lista de produtos
products = [
    {"nome": "Notebook", "preco": 3500},
    {"nome": "Smartphone", "preco": 2000},
    {"nome": "Tênis", "preco": 300}
]

# Carrinho de compras (lista vazia no início)
cart = []

def show_products():
    """Exibe a lista de produtos disponíveis com um índice"""
    print("\nLista de Produtos Disponíveis:")
    for i, p in enumerate(products, start=1):  # O índice começa em 1
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
    """Exibe os itens no carrinho e o total da compra"""
    if not cart:
        print("\nSeu carrinho está vazio!\n")
        return

    print("\n=== Carrinho de Compras ===")
    total = 0
    for i, item in enumerate(cart, start=1):
        print(f"{i} - {item['nome']} | R${item['preco']}")
        total += item['preco']
    
    print(f"\nTotal da compra: R${total}")

def checkout():
    """Finaliza a compra e limpa o carrinho"""
    if not cart:
        print("\nSeu carrinho está vazio! Adicione produtos antes de finalizar a compra.\n")
        return

    view_cart()
    confirm = input("\nDeseja finalizar a compra? (s/n): ").strip().lower()
    
    if confirm == "s":
        print("\nCompra finalizada com sucesso! Obrigado por comprar conosco.\n")
        cart.clear()  # Esvazia o carrinho
    else:
        print("\nCompra não finalizada. Você pode continuar comprando.\n")

while True:
    print("\n=== Menu ===")
    print("1 - Cadastrar Usuário")
    print("2 - Fazer Login")
    print("3 - Sair")

    option = input("Escolha uma opção: ")

    if option == "1":
        # Cadastro
        user = input("Cadastre um nome de usuário: ")
        password = input("Cadastre uma senha: ")
        print("Usuário cadastrado com sucesso!\n")

    elif option == "2":
        # Login
        if user is None:
            print("Nenhum usuário cadastrado. Cadastre-se primeiro!")
            continue

        user_input = input("Digite seu usuário: ")
        password_input = input("Digite sua senha: ")

        if user_input == user and password_input == password:
            print("Login bem-sucedido!")
            logged = True  # Marca que o usuário está logado

            while logged:
                print("\n=== Menu do Usuário ===")
                print("1 - Ver Produtos")
                print("2 - Comprar ou Adicionar ao Carrinho")
                print("3 - Ver Carrinho")
                print("4 - Finalizar Compra")
                print("5 - Logout")

                option_user = input("Escolha uma opção: ")

                if option_user == "1":
                    show_products()
                elif option_user == "2":
                    buy_or_add_to_cart()
                elif option_user == "3":
                    view_cart()
                elif option_user == "4":
                    checkout()
                elif option_user == "5":
                    print("Você saiu da conta.")
                    logged = False  # Sai do loop e retorna ao menu principal
                else:
                    print("Opção inválida! Escolha entre 1 e 5.")

        else:
            print("Usuário ou senha incorretos.")

    elif option == "3":
        print("Saindo...")
        break

    else:
        print("Opção inválida! Escolha 1, 2 ou 3.")
