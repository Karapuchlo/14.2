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
        if type(self) != type(other):
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


class Smartphone(Product):
    def __init__(self, name, description, price, quantity, screen_size, model, memory, color):
        super().__init__(name, description, price, quantity)
        self.screen_size = screen_size
        self.model = model
        self.memory = memory
        self.color = color

    def __str__(self):
        return f"{self.name}, {self.price:.2f} руб. Остаток: {self.quantity} шт."

    @property
    def efficiency(self):
        # Вычисление efficiency на основе других атрибутов
        return self.screen_size / self.memory


class LawnGrass(Product):
    def __init__(self, name, description, price, quantity, country, germination_period, color):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color

    def __str__(self):

        return f"{self.name}, {self.price:.2f} руб. Остаток: {self.quantity} шт."

        required_keys = ['name', 'price', 'quantity']
        for key in required_keys:
            if key not in product_data:
                raise ValueError(f"Отсутствует обязательный ключ: {key}")
        return cls(product_data['name'], product_data['description'], product_data['price'], product_data['quantity'])

