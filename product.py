from abc import ABC, abstractmethod
from logging_mixin import LoggingMixin


class Representable:
    def __repr__(self):
        pass
class BaseProduct(LoggingMixin, Representable, ABC):
    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity
        print(f"Создан новый объект продукта: {self.name}")

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
        return cls(product_data['name'], product_data['description'], product_data['price'], product_data['quantity'])

    @abstractmethod
    def apply_discount(self, discount):
        pass

class Product(BaseProduct):
    def apply_discount(self, discount):
        self.price = self.price * (1 - discount)

class LawnGrass(Product):
    def apply_discount(self, discount):
        self.price = self.price * (1 - discount)

class Smartphone(Product):
    def apply_discount(self, discount):
        self.price = self.price * (1 - discount)

