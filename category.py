from product import Product

class Category:
    def __init__(self, name, description, products=None):
        self.name = name
        self.description = description
        if products is None:
            self._products = []
        else:
            self._products = products

    def add_product(self, product):
        self._products.append(product)

    @property
    def product_count(self):
        return len(self._products)

    @property
    def products(self):
        return [f"{p.name}, {p.price}, {p.quantity}" for p in self._products]
