class Category:

    def __init__(self, name, description, products=None):
        self.name = name
        self.description = description
        self._products = []
        if products:
            for product in products:
                self.add_product(product)


    def add_product(self, product):
        self._products.append(product)

    @property
    def products(self):
        return [f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт." for product in self._products]


    def __str__(self):
        total_quantity = sum(product.quantity for product in self._products)
        product_list = "\n".join(self.products)
        return f"{self.name}, {self.description}, количество продуктов: {total_quantity} шт."



