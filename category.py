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

    def middle_price(self):
        if not self.products:
            return 0
        try:
            total_price = sum(product.price for product in self.products)
            return total_price / len(self.products)
        except ZeroDivisionError:
            return 0

    @property
    def product_count(self):
        return len(self._products)

    @property
    def products(self):
        return self._products

    def __repr__(self):
        product_reprs = [repr(product) for product in self._products]
        return f"Category('{self.name}', '{self.description}', [{', '.join(product_reprs)}])"
