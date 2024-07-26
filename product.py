class Product:
    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity
        #self.color = color

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
        required_keys = ['name', 'price', 'quantity']
        for key in required_keys:
            if key not in product_data:
                raise ValueError(f"Отсутствует обязательный ключ: {key}")
        return cls(product_data['name'], product_data['description'], product_data['price'], product_data['quantity'])