carrinho = []
while True:
    print('-- Seja bem-vindo ao menu --')
    print('1 - Adicionar produto')
    print('2 - Editar produto')
    print('3 - Remover produto')
    print('4 - Listar todos os produtos')
    print('5 - Sair')
    opcao = input('Digite a opção desejada: ')
    if opcao == '1':
        produto = input('Digite o nome do produto: ')
        carrinho.append(produto)
        print('Produto adicionado com sucesso!')
    elif opcao == '2':
        produto = input('Digite o produto que deseja editar: ')
        if produto in carrinho:
            indice = carrinho.index(produto)
            carrinho[indice] = input('Digite o novo nome do produto: ')
            print('Produto editado com sucesso!')
        else:
            print('PRODUTO NÃO ENCONTRADO!')
    elif opcao == '3':
        produto = input('Digite o produto que deseja remover: ')
        if produto in carrinho:
            carrinho.remove(produto)
            print('Produto REMOVIDO com sucesso!')
        else:
            print('PRODUTO NÃO ENCONTRADO!')
    elif opcao == '4':
        print('---- SEU CARRINHO ----')
        for produto in carrinho:
            print(f'Nome do produto: {produto}')
    elif opcao == '5':
        print('O programa foi encerrado!')
        break