from abc import ABC, abstractmethod

class Representable(ABC):
    @abstractmethod
    def __repr__(self):
        """Должен возвращать строку"""
        pass

class BaseProduct(Representable, ABC):
    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
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
        return cls(product_data['name'], product_data['description'], product_data['price'], product_data['quantity'])

    @abstractmethod
    def apply_discount(self, discount):
        pass

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', '{self.description}', {self.__price}, {self.quantity})"

class Product(BaseProduct):
    def apply_discount(self, discount):
        self.__price = self.__price * (1 - discount)

class LawnGrass(Product):
    pass

class Smartphone(Product):
    pass
