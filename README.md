# agil-store-cli

## Descrição

Sistema de Gerenciamento de Produtos para a Loja AgilStore; desenvolvido em Python, que permite adicionar, listar, atualizar, excluir e buscar produtos em um inventário. Os dados dos produtos são persistidos em um arquivo JSON.

## Tecnologias Utilizadas

- Python 3.9+
- `colorama` para adicionar cores ao terminal (uso opcional)
- `json` para persistência de dados, com salvamento automático para que os produtos não sejam perdidos ao encerrar a aplicação
- `uuid` para gerar IDs únicos para cada produto

## Estrutura do Projeto

```
agil-store-api/
├── data/
│   └── products.json
├── store/
│   ├── __init__.py
│   ├── product.py
│   ├── store.py
│   └── utils.py
├── LICENSE
├── main.py
├── README.md
└── requirements.txt
```

## Instalação

### Pré-requisitos

- Python 3.9 ou superior instalado.

### Clonar o Repositório

```sh
git clone https://github.com/gabrielricardo7/agil-store-cli.git
cd agil-store-cli
```

### Criar e Ativar um Ambiente Virtual (opcional, mas recomendado):

```sh
python -m venv "venv" && source venv/bin/activate
```

### Instalar a biblioteca "colorama" (opcional, se quiser cores):

```sh
pip install -r requirements.txt
```

#### ou

```sh
pip install colorama
```

## Executar a Aplicação

### Passos para rodar o sistema:

1. Certifique-se de que está no diretório raiz do projeto:

```sh
cd agil-store-cli
```

2. Execute o script `main.py`:

```sh
python main.py
```

## Funcionalidades

### 1. Adicionar Produto

Permite ao usuário adicionar um novo produto ao inventário.

- Solicita ao usuário a inserção dos seguintes dados:
  - Nome do Produto
  - Categoria
  - Quantidade em Estoque
  - Preço
- Gera um ID único para cada produto automaticamente.

### 2. Listar Produtos

Exibe todos os produtos cadastrados no inventário em formato de tabela.

- Mostra uma tabela com as seguintes colunas:
  - ID
  - Nome do Produto
  - Categoria
  - Quantidade em Estoque
  - Preço
- Permite opções de filtragem por categoria ou ordenação por nome, quantidade ou preço.

### 3. Atualizar Produto

Atualiza as informações de um produto existente identificado pelo seu ID.

- Verifica se o ID informado existe no inventário.
- Solicita ao usuário quais campos deseja atualizar (Nome, Categoria, Quantidade, Preço).
- Valida os novos dados antes de salvar as alterações.

### 4. Excluir Produto

Remove um produto do inventário pelo seu ID.

- Verifica se o ID informado existe no inventário.
- Confirma a ação com o usuário antes de excluir.
- Remove o produto do inventário após a confirmação.

### 5. Buscar Produto

Busca e exibe detalhes de um produto específico pelo ID ou pelo nome.

- Permite a busca por ID ou por parte do nome do produto.
- Exibe todas as informações detalhadas do produto encontrado.
- Exibe mensagem apropriada se nenhum produto for encontrado.

## Licença

Este projeto é licenciado sob os termos da licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.
