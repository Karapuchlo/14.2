
from product import *


class Category:

    product_count = None

    def __init__(self, name, description, products=None):
        self.name = name
        self.description = description

        if products is None:
            self._products = []
        else:
            self._products = products

    def add_product(self, product):
        self._products.append(product)

    @staticmethod
    def get_product_count(category):
        return category._product_count

    @property

    def product_count(self):
        return len(self._products)

    @property
    def products(self):
        return [f"{p.name}, {p.price}, {p.quantity}" for p in self._products]

    def __str__(self):
        total_quantity = sum(product.quantity for product in self.__products)
        product_list = "\n".join(self.products)
        return f"{self.name}, {self.description}, количество продуктов: {total_quantity} шт."

    @products.setter
    def products(self, value):
        self.__products = value

