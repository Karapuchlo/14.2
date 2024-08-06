from product import *

class Category:

    product_count = None

    def __init__(self, name, description, products=None):
        self.name = name
        self.description = description
        self.__products = products
        self._product_count = len(products)


    def add_product(self, product):
        if not isinstance(product, Product) and not issubclass(type(product), Product):
            raise TypeError("Можно добавлять только продукты или их наследников")
        self.__products.append(product)
        self._product_count += 1

    @staticmethod
    def get_product_count(category):
        return category._product_count

    @property
    def products(self):
        return [f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт." for product in self.__products]


    def __str__(self):
        total_quantity = sum(product.quantity for product in self.__products)
        product_list = "\n".join(self.products)
        return f"{self.name}, {self.description}, количество продуктов: {total_quantity} шт."

    @products.setter
    def products(self, value):
        self.__products = value



