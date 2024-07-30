class Category:
    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self._products = products

    def add_product(self, product):
        self._products.append(product)

    @property
    def products(self):
        return [f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт." for product in self._products]

    def __str__(self):
        total_quantity = sum(product.quantity for product in self._products)
        product_list = "\n".join(self.products)
        return f"{self.name}, {self.description}, количество продуктов: {total_quantity} шт."

class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.__price = price
        self.quantity = quantity

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price):
        if new_price <= 0:
            raise ValueError("Цена должна быть больше нуля.")
        self.__price = new_price

    @classmethod
    def new_product(cls, product_data):
        return cls(product_data['name'], product_data['price'], product_data['quantity'])
