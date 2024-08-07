class Category:
    def __init__(self, name, description, products=None):
        self.name = name
        self.description = description
        self._products = products if products else []
        self._product_count = len(self._products)

    def add_product(self, product):
        self._products.append(product)
        self._product_count += 1

    @property
    def products(self):
        return [f"{p.name}, {p.price} руб. Остаток: {p.quantity} шт." for p in self._products]

    @property
    def product_count(self):
        return self._product_count
