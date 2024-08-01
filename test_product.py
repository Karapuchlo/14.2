import pytest
from product import Product
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

if __name__ == "__main__":
    pytest.main()
