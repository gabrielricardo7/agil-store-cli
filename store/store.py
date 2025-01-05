from .product import Product
import json


class Store:
    def __init__(self, json_file):
        self.json_file = json_file
        self.products = self.load_products()

    def load_products(self):
        try:
            with open(self.json_file, 'r') as file:
                products = json.load(file)
                return [Product.from_dict(prod) for prod in products]
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def save_products(self):
        with open(self.json_file, 'w') as file:
            json.dump([prod.to_dict()
                      for prod in self.products], file, indent=4)

    def add_product(self, product):
        self.products.append(product)
        self.save_products()

    def list_products(self, filter_by=None, sort_by=None):
        if filter_by:
            filtered = [
                prod for prod in self.products if prod.categoria.lower() == filter_by.lower()]
        else:
            filtered = self.products

        if sort_by:
            sort_by = sort_by.lower()
            if sort_by == "nome":
                filtered = sorted(filtered, key=lambda x: x.nome)
            elif sort_by == "quantidade" or sort_by == "quant":
                filtered = sorted(
                    filtered, key=lambda x: x.quantidade_em_estoque)
            elif sort_by == "preco":
                filtered = sorted(filtered, key=lambda x: x.preco)

        return filtered

    def get_product(self, product_id):
        for prod in self.products:
            if prod.id == product_id:
                return prod
        return None

    def search_products(self, search_term):
        results = [prod for prod in self.products if search_term.lower(
        ) in prod.nome.lower() or prod.id == search_term]
        return results

    def update_product(self, product_id, nome=None, categoria=None, quantidade_em_estoque=None, preco=None):
        product = self.get_product(product_id)
        if product:
            if nome:
                product.nome = nome
            if categoria:
                product.categoria = categoria
            if quantidade_em_estoque:
                product.quantidade_em_estoque = quantidade_em_estoque
            if preco:
                product.preco = preco
            self.save_products()

    def delete_product(self, product_id):
        self.products = [
            prod for prod in self.products if prod.id != product_id]
        self.save_products()
