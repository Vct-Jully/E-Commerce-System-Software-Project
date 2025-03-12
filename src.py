from abc import ABC, abstractmethod

# Classe Abstrata
class Usuario(ABC):
    def __init__(self, usuario, senha):
        self.usuario = usuario
        self.senha = senha

    def autenticar(self, usuario, senha):
        return self.usuario == usuario and self.senha == senha

    @abstractmethod
    def menu(self):
        pass  # Método obrigatório a ser implementado


# Classe Administrador (Herança de Usuario)
class Administrador(Usuario):
    def menu(self):
        while True:
            print("\n=== Menu de Administração ===")
            print("1 - Adicionar Produto")
            print("2 - Editar Produto")
            print("3 - Remover Produto")
            print("4 - Logout")
            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                nome = input("Digite o nome do produto: ")
                preco = float(input("Digite o preço do produto: R$"))
                products.append({"nome": nome, "preco": preco})
                print(f"Produto {nome} adicionado!")

            elif opcao == "2":
                show_products()
                index = int(input("Digite o número do produto a ser editado: ")) - 1
                if 0 <= index < len(products):
                    nome = input("Digite o novo nome do produto: ")
                    preco = float(input("Digite o novo preço do produto: R$"))
                    products[index] = {"nome": nome, "preco": preco}
                    print("Produto atualizado!")

            elif opcao == "3":
                show_products()
                index = int(input("Digite o número do produto a ser removido: ")) - 1
                if 0 <= index < len(products):
                    removed_product = products.pop(index)
                    print(f"Produto {removed_product['nome']} removido!")

            elif opcao == "4":
                print("Saindo do menu de administração...")
                break

            else:
                print("Opção inválida!")


# Classe Cliente (Herança de Usuario)
class Cliente(Usuario):
    def __init__(self, usuario, senha):
        super().__init__(usuario, senha)
        self.carrinho = []

    def menu(self):
        while True:
            print("\n=== Menu do Cliente ===")
            print("1 - Ver Produtos")
            print("2 - Comprar ou Adicionar ao Carrinho")
            print("3 - Gerenciar Carrinho")
            print("4 - Logout")
            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                show_products()
            elif opcao == "2":
                comprar_ou_adicionar(self.carrinho)
            elif opcao == "3":
                gerenciar_carrinho(self.carrinho)
            elif opcao == "4":
                print("Logout realizado.")
                break
            else:
                print("Opção inválida!")


# Lista de usuários e produtos
admins = [Administrador("admin", "admin123"), Administrador("gestor", "gestor123")]
users = []
products = [
    {"nome": "Notebook", "preco": 3500},
    {"nome": "Smartphone", "preco": 2000},
    {"nome": "Tênis", "preco": 300}
]


# Funções auxiliares
def show_products():
    print("\nLista de Produtos Disponíveis:")
    for i, p in enumerate(products, start=1):
        print(f"{i} - Nome: {p['nome']}, Preço: R${p['preco']}")


def selecionar_metodo_pagamento():
    print("\nEscolha o método de pagamento:")
    print("1 - Pix")
    print("2 - Boleto")
    print("3 - Cartão de Crédito")
    opcao = input("Opção: ")
    if opcao == "1":
        return "Pix"
    elif opcao == "2":
        return "Boleto"
    elif opcao == "3":
        return "Cartão de Crédito"
    else:
        print("Opção inválida, tente novamente.")
        return selecionar_metodo_pagamento()


def comprar_ou_adicionar(cart):
    show_products()
    choice = int(input("Digite o número do produto desejado: ")) - 1
    if 0 <= choice < len(products):
        print("1 - Comprar agora")
        print("2 - Adicionar ao carrinho")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            metodo = selecionar_metodo_pagamento()
            print(f"Compra realizada via {metodo}! Produto: {products[choice]['nome']} - R${products[choice]['preco']}")
        elif opcao == "2":
            cart.append(products[choice])
            print(f"{products[choice]['nome']} adicionado ao carrinho!")
        else:
            print("Opção inválida.")
    else:
        print("Produto inválido.")


def gerenciar_carrinho(cart):
    while True:
        print("\n=== Gerenciar Carrinho ===")
        print("1 - Ver Carrinho")
        print("2 - Remover Item")
        print("3 - Remover Todos os Itens")
        print("4 - Comprar Item Específico")
        print("5 - Comprar Todos os Itens")
        print("6 - Voltar")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            view_cart(cart)
        elif opcao == "2":
            view_cart(cart)
            remover_item(cart)
        elif opcao == "3":
            cart.clear()
            print("Todos os itens foram removidos do carrinho.")
        elif opcao == "4":
            view_cart(cart)
            comprar_item_especifico(cart)
        elif opcao == "5":
            comprar_todos_os_itens(cart)
        elif opcao == "6":
            break
        else:
            print("Opção inválida!")


def view_cart(cart):
    if not cart:
        print("Seu carrinho está vazio!")
    else:
        print("\n=== Carrinho ===")
        for i, item in enumerate(cart, start=1):
            print(f"{i} - {item['nome']} | R${item['preco']}")


def remover_item(cart):
    if not cart:
        print("Carrinho vazio.")
        return

    index = int(input("Digite o número do item a ser removido: ")) - 1
    if 0 <= index < len(cart):
        removed_item = cart.pop(index)
        print(f"Item {removed_item['nome']} removido do carrinho.")
    else:
        print("Número inválido.")


def comprar_item_especifico(cart):
    if not cart:
        print("Carrinho vazio.")
        return

    index = int(input("Digite o número do item a ser comprado: ")) - 1
    if 0 <= index < len(cart):
        item = cart.pop(index)
        metodo = selecionar_metodo_pagamento()
        print(f"Compra realizada via {metodo}! Produto: {item['nome']} - R${item['preco']}")
    else:
        print("Número inválido.")


def comprar_todos_os_itens(cart):
    if not cart:
        print("Carrinho vazio.")
        return

    metodo = selecionar_metodo_pagamento()
    total = sum(item["preco"] for item in cart)
    cart.clear()
    print(f"Compra total de R${total:.2f} realizada via {metodo}!")


def login():
    usuario = input("Usuário: ")
    senha = input("Senha: ")

    for admin in admins:
        if admin.autenticar(usuario, senha):
            print(f"Login bem-sucedido como Administrador: {admin.usuario}")
            admin.menu()
            return

    for user in users:
        if user.autenticar(usuario, senha):
            print(f"Login bem-sucedido! Usuário: {user.usuario}")
            user.menu()
            return

    print("Usuário ou senha incorretos.")


def cadastrar_usuario():
    usuario = input("Novo usuário: ")
    senha = input("Senha: ")
    users.append(Cliente(usuario, senha))
    print("Usuário cadastrado!")


while True:
    print("\n=== Menu ===")
    print("1 - Fazer Login")
    print("2 - Cadastrar Usuário")
    print("3 - Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        login()
    elif opcao == "2":
        cadastrar_usuario()
    elif opcao == "3":
        print("Saindo...")
        break
    else:
        print("Opção inválida!")
