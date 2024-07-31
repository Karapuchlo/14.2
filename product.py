class Product:
    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity
        # self.color = color

    def __str__(self):
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        if not isinstance(other, Product):
            raise TypeError("Can only add Product objects")
        total_value = self.price * self.quantity + other.price * other.quantity
        return total_value

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
