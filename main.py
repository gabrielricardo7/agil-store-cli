from store.store import Store
from store.product import Product
from store.utils import convert_comma_to_dot, detail_prod, request_input, truncate_string, wait_to_continue, Fore, Back, Style


def main():
    store = Store("data/products.json")

    while True:
        print(
            f"\n{Fore.LIGHTYELLOW_EX}Sistema de Gerenciamento de Produtos da Loja AgilStore")
        print(f"{Fore.GREEN}1. Adicionar Produto")
        print(f"{Fore.GREEN}2. Listar Produtos")
        print(f"{Fore.GREEN}3. Atualizar Produto")
        print(f"{Fore.GREEN}4. Excluir Produto")
        print(f"{Fore.GREEN}5. Buscar Produto")
        print(f"{Fore.RED}6. Sair")
        escolha = input(
            f"{Fore.LIGHTCYAN_EX}Selecione uma opção: "+Style.RESET_ALL)

        if escolha == '1':
            nome = request_input("\nDigite o nome do produto: ", 'str')
            while store.get_product_by_name(nome):
                print(f"{Fore.RED}Erro: Produto com o nome '{nome}' já existe.")
                nome = request_input("Digite o nome do produto: ", 'str')
            categoria = request_input(
                "Digite a categoria do produto: ", 'str')
            quantidade_em_estoque = request_input(
                "Digite a quantidade em estoque: ", 'int')
            preco = request_input("Digite o preço do produto: ", 'float')

            quantidade_em_estoque = int(quantidade_em_estoque)
            preco = float(convert_comma_to_dot(preco))

            product = Product(nome, categoria, quantidade_em_estoque, preco)
            store.add_product(product)
            print(f"\n{Fore.GREEN}Produto adicionado com sucesso!")
            if product:
                detail_prod(product, show_id=True)
            wait_to_continue()
        elif escolha == '2':
            filter_by = input(
                "\nFiltrar por categoria (deixe em branco para não filtrar): ")
            sort_by = input(
                "Ordenar por (nome, quantidade, preco ou deixe em branco para não ordenar): ")
            products = store.list_products(
                filter_by if filter_by else None, sort_by if sort_by else None)
            print(
                f"\n{Fore.LIGHTYELLOW_EX}{Back.BLUE}{'ID':<36} {'Nome':<29} {'Categoria':<15} {'Quantidade':<10} {'Preço (R$)':<10}")
            fc = True
            for prod in products:
                nome_truncado = truncate_string(prod.nome, 29)
                print(
                    f"{Fore.BLACK if fc else Fore.WHITE}{Back.LIGHTYELLOW_EX if fc else Back.BLUE}{prod.id:<36} {nome_truncado:<29} {prod.categoria:<15} {prod.quantidade_em_estoque:>10} {prod.preco:>10.2f}")
                fc = not fc
            wait_to_continue()
        elif escolha == '3':
            id = input("\nDigite o ID do produto: ")
            product = store.get_product(id)
            if product:
                detail_prod(product)
                nome = request_input(
                    "Digite o novo nome (deixe em branco para manter o atual): ", 'str', obrigatorio=False)
                while nome != None and store.get_product_by_name(nome):
                    print(f"{Fore.RED}Erro: Produto com o nome '{
                          nome}' já existe.")
                    nome = request_input(
                        "Digite o novo nome (deixe em branco para manter o atual): ", 'str', obrigatorio=False)
                categoria = request_input(
                    "Digite a nova categoria (deixe em branco para manter a atual): ", 'str', obrigatorio=False)
                quantidade_em_estoque = request_input(
                    "Digite a nova quantidade em estoque (deixe em branco para manter o atual): ", 'int', obrigatorio=False)
                preco = request_input(
                    "Digite o novo preço (deixe em branco para manter o atual): ", 'float', obrigatorio=False)

                quantidade_em_estoque = int(
                    quantidade_em_estoque) if quantidade_em_estoque else None

                preco = float(convert_comma_to_dot(preco)) if preco else None

                store.update_product(
                    id,
                    nome=nome if nome else None,
                    categoria=categoria if categoria else None,
                    quantidade_em_estoque=int(
                        quantidade_em_estoque) if quantidade_em_estoque else None,
                    preco=float(preco) if preco else None
                )
                print(f"{Fore.GREEN}Produto atualizado com sucesso!")
            else:
                print(f"{Fore.RED}Produto não encontrado.")
            wait_to_continue()
        elif escolha == '4':
            id = input("\nDigite o ID do produto: ")
            product = store.get_product(id)
            if product:
                detail_prod(product)
                confirm = input(
                    "Tem certeza que deseja excluir este produto? (s/n): ")
                if confirm.lower() == 's':
                    store.delete_product(id)
                    print(f"{Fore.GREEN}Produto excluído com sucesso.")
                else:
                    print(f"{Fore.YELLOW}Ação cancelada.")
            else:
                print(f"{Fore.RED}Produto não encontrado.")
            wait_to_continue()
        elif escolha == '5':
            search_term = input("\nDigite o ID ou parte do nome do produto: ")
            results = store.search_products(search_term)
            if results:
                fc = True
                for prod in results:
                    print(
                        f"{Fore.LIGHTRED_EX if fc else Fore.LIGHTMAGENTA_EX}{prod.to_dict()}")
                    fc = not fc
            else:
                print(f"{Fore.RED}Produto não encontrado.")
            wait_to_continue()
        elif escolha == '6':
            exit()
        else:
            print(f"{Fore.RED}Opção inválida. Tente novamente.")
            wait_to_continue()


if __name__ == "__main__":
    while True:
        try:
            main()
        except KeyboardInterrupt:
            restart = input(
                f"\n{Fore.MAGENTA}Execução interrompida pelo usuário. \nDeseja reiniciar a aplicação? (s/n):"+Style.RESET_ALL+" ").lower()
            if restart != 's':
                print(f"{Fore.RED}Aplicação encerrada.")
                break
