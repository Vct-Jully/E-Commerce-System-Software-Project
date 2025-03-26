# E-Commerce-System---Software-Project

## Descrição
Este projeto é um sistema de e-commerce desenvolvido em Python utilizando Programação Orientada a Objetos (POO). Este sistema permite que administradores adicionem, editem e removam produtos, enquanto clientes podem visualizar, adicionar ao carrinho e comprar produtos. O sistema utiliza um mecanismo de autenticação simples e um menu interativo baseado em terminal.


## Funções não implementadas
Compra à distância e rastreamento do pedido, descontos/promoções e um sistema de avaliação/reclamação dos produtos.

## Classes e Variáveis Principais

### Classe `Usuario`
Classe abstrata que representa um usuário do sistema.

#### Atributos:
- `usuario`: Nome de usuário.
- `senha`: Senha do usuário.

#### Métodos:
- `autenticar(usuario, senha)`: Verifica se as credenciais fornecidas correspondem às do usuário.
- `menu()`: Método abstrato que deve ser implementado pelas classes filhas.

### Classe `Administrador` (Herda de `Usuario`)
Usuário com permissão para gerenciar produtos.

#### Métodos:
- `menu()`: Exibe o menu de administração com as opções:
  - Adicionar Produto
  - Editar Produto
  - Remover Produto
  - Logout
  
- `adicionar_produto(nome, preco)`: Adiciona um novo produto à lista de produtos.
- `editar_produto(nome_antigo, nome_novo, preco_novo)`: Edita um produto existente.
- `remover_produto(nome)`: Remove um produto da lista.

### Classe `Cliente` (Herda de `Usuario`)
Usuário que pode comprar produtos e gerenciar um carrinho de compras.

#### Atributos:
- `carrinho`: Lista de produtos adicionados para compra.

#### Métodos:
- `menu()`: Exibe o menu do cliente com opções para:
  - Ver produtos
  - Comprar ou adicionar produtos ao carrinho
  - Gerenciar carrinho
  - Logout
  
- `adicionar_ao_carrinho(nome)`: Adiciona um produto ao carrinho.
- `remover_do_carrinho(nome)`: Remove um item do carrinho.
- `finalizar_compra()`: Processa a compra dos itens no carrinho.

## Listas Globais
- `admins`: Lista contendo os administradores do sistema.
- `users`: Lista de clientes cadastrados.
- `products`: Lista de dicionários representando os produtos disponíveis, com `nome` e `preco`.

## Funções Auxiliares
- `show_products()`: Exibe os produtos disponíveis.
- `selecionar_metodo_pagamento()`: Solicita ao usuário a escolha de um método de pagamento.
- `comprar_ou_adicionar(cart)`: Permite que o cliente compre ou adicione produtos ao carrinho.
- `gerenciar_carrinho(cart)`: Exibe opções para visualizar, remover ou comprar itens do carrinho.
- `view_cart(cart)`: Exibe o conteúdo do carrinho do cliente.
- `remover_item(cart)`: Permite remover um item específico do carrinho.
- `comprar_item_especifico(cart)`: Compra um item específico do carrinho.
- `comprar_todos_os_itens(cart)`: Compra todos os itens do carrinho.
- `login()`: Permite que administradores e clientes façam login.
- `cadastrar_usuario()`: Cadastra um novo cliente.

## Fluxo do Programa
1. O sistema exibe um menu principal com opções para login, cadastro de usuário ou saída.
2. Usuários fazem login e acessam seus respectivos menus.
3. Administradores podem gerenciar produtos.
4. Clientes podem visualizar produtos, gerenciar carrinho e realizar compras.
5. O sistema mantém a execução até que o usuário escolha sair.

## Execução
Basta rodar o script em um ambiente Python (versão 3+). O sistema interage via terminal e não requer bibliotecas externas.

