from abc import ABC, abstractmethod

class BaseProduct(ABC):
    @abstractmethod
    def new_product(self, *args):
        pass

class LoggingMixin:
    def __init__(self, *args):
        print(repr(self))

    def __repr__(self):
        object_attributes = ', '.join(f'{k}: {v}' for k, v in self.__dict__.items())
        return f"Создан объект со свойствами {object_attributes}"

class Product(BaseProduct, LoggingMixin):
    """
    Класс для описания товара в магазине
    """
    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        if quantity <= 0:
            raise ValueError("Товар с нулевым количеством не может быть добавлен")
        self.quantity = quantity
        super().__init__()

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price):
        if new_price <= 0:
            raise ValueError("Цена должна быть больше нуля.")
        self.__price = new_price

    def apply_discount(self, discount):
        self.__price = self.__price * (1 - discount)

    @classmethod
    def new_product(cls, product_data):
        return cls(**product_data)


class LawnGrass(Product):
    @classmethod
    def new_product(cls, product_data):
        return cls(**product_data)


class Smartphone(Product):
    @classmethod
    def new_product(cls, product_data):
        return cls(**product_data)
