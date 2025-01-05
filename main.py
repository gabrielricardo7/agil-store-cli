from store.store import Store
from store.product import Product


def convert_comma_to_dot(value):
    return value.replace(',', '.')


def truncate_string(string, max_length):
    return string if len(string) <= max_length else string[:max_length - 3] + '...'


def main():
    store = Store("data/products.json")

    while True:
        print("\nSistema de Gerenciamento de Produtos da Loja AgilStore")
        print("1. Adicionar Produto")
        print("2. Listar Produtos")
        print("3. Atualizar Produto")
        print("4. Excluir Produto")
        print("5. Buscar Produto")
        print("6. Sair")
        escolha = input("Selecione uma opção: ")

        if escolha == '1':
            nome = input("Digite o nome do produto: ")
            categoria = input("Digite a categoria do produto: ")
            quantidade_em_estoque = int(convert_comma_to_dot(
                input("Digite a quantidade em estoque: ")))
            preco = float(convert_comma_to_dot(
                input("Digite o preço do produto: ")))
            store.add_product(
                Product(nome, categoria, quantidade_em_estoque, preco))
        elif escolha == '2':
            filter_by = input(
                "Filtrar por categoria (deixe em branco para não filtrar): ")
            sort_by = input(
                "Ordenar por (nome, quantidade, preco, deixe em branco para não ordenar): ")
            products = store.list_products(
                filter_by if filter_by else None, sort_by if sort_by else None)
            print(
                f"{'ID':<36} {'Nome':<29} {'Categoria':<15} {'Quantidade':<10} {'Preço':<10}")
            for prod in products:
                nome_truncado = truncate_string(prod.nome, 29)
                print(
                    f"{prod.id:<36} {nome_truncado:<29} {prod.categoria:<15} {prod.quantidade_em_estoque:<10} R$ {prod.preco:<10.2f}")
        elif escolha == '3':
            id = input("Digite o ID do produto: ")
            if store.get_product(id):
                nome = input(
                    "Digite o novo nome (deixe em branco para manter o atual): ")
                categoria = input(
                    "Digite a nova categoria (deixe em branco para manter a atual): ")
                quantidade_em_estoque = convert_comma_to_dot(input(
                    "Digite a nova quantidade em estoque (deixe em branco para manter o atual): "))
                preco = convert_comma_to_dot(
                    input("Digite o novo preço (deixe em branco para manter o atual): "))
                store.update_product(
                    id,
                    nome=nome if nome else None,
                    categoria=categoria if categoria else None,
                    quantidade_em_estoque=int(
                        quantidade_em_estoque) if quantidade_em_estoque else None,
                    preco=float(preco) if preco else None
                )
            else:
                print("Produto não encontrado.")
        elif escolha == '4':
            id = input("Digite o ID do produto: ")
            if store.get_product(id):
                confirm = input(
                    "Tem certeza que deseja excluir este produto? (s/n): ")
                if confirm.lower() == 's':
                    store.delete_product(id)
                    print("Produto excluído com sucesso.")
                else:
                    print("Ação cancelada.")
            else:
                print("Produto não encontrado.")
        elif escolha == '5':
            search_term = input("Digite o ID ou parte do nome do produto: ")
            results = store.search_products(search_term)
            if results:
                for prod in results:
                    print(prod.to_dict())
            else:
                print("Produto não encontrado.")
        elif escolha == '6':
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()
