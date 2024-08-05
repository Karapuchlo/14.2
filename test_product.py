import pytest
from product import *
from category import Category

def test_product_string_representation():
    product = Product("Apple", 'яблоко', 80, 20)
    assert str(product) == "Apple, 80 руб. Остаток: 20 шт."

def test_category_string_representation():
    products = [
        Product("Apple", 'яблоко', 10, 15),
        Product("Banana", 'бананы', 20, 15),
        Product("Orange", 'апельсины', 15, 15)
    ]
    category = Category("Fruits", 'фрукты', products)
    assert str(category) == "Fruits, фрукты, количество продуктов: 45 шт."

def test_product_addition():
    product1 = Product("Apple", 'яблоко', 80, 5)
    product2 = Product("Banana", 'бананы', 50, 10)
    total_value = product1 + product2
    assert total_value == 900

def test_smartphone_creation():
    smartphone = Smartphone("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5, 95.5, "S23 Ultra", 256, "Серый")
    assert smartphone.name == "Samsung Galaxy S23 Ultra"
    assert smartphone.description == "256GB, Серый цвет, 200MP камера"
    assert smartphone.price == 180000.0
    assert smartphone.quantity == 5
    assert smartphone.model == "S23 Ultra"
    assert smartphone.color == "Серый"

def test_smartphone_str_representation():
    smartphone = Smartphone("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5, 95.5, "S23 Ultra", 256, "Серый")
    assert str(smartphone) == "Samsung Galaxy S23 Ultra, 180000.00 руб. Остаток: 5 шт."

def test_smartphone_addition():
    smartphone1 = Smartphone("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5, 95.5, "S23 Ultra", 256, "Серый")
    smartphone2 = Smartphone("Iphone 15", "512GB, Gray space", 210000.0, 8, 98.2, "15", 512, "Gray space")
    smartphone_sum = smartphone1 + smartphone2
    assert isinstance(smartphone_sum, Smartphone)
    assert smartphone_sum.price == 390000.0
    assert smartphone_sum.quantity == 13
    assert smartphone_sum.name == "Samsung Galaxy S23 Ultra + Iphone 15"
    assert smartphone_sum.description == "256GB, Серый цвет, 200MP камера + 512GB, Gray space"
    assert smartphone_sum.model == "S23 Ultra + 15"
    assert smartphone_sum.color == "Серый + Gray space"


if __name__ == "__main__":
    pytest.main()
