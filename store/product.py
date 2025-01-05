import uuid


class Product:
    def __init__(self, nome, categoria, quantidade_em_estoque, preco):
        self.id = str(uuid.uuid4())
        self.nome = nome
        self.categoria = categoria
        self.quantidade_em_estoque = quantidade_em_estoque
        self.preco = preco

    def to_dict(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "categoria": self.categoria,
            "quantidade_em_estoque": self.quantidade_em_estoque,
            "preco": self.preco
        }

    @classmethod
    def from_dict(cls, data):
        produto = cls(
            data["nome"],
            data["categoria"],
            data["quantidade_em_estoque"],
            data["preco"]
        )
        produto.id = data["id"]
        return produto
