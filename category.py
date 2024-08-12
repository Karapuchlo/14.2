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
        return self._products

    def __repr__(self):
        product_reprs = [repr(product) for product in self._products]
        return f"Category('{self.name}', '{self.description}', {product_reprs})"

