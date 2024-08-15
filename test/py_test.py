import pytest
from product import Product
from category import Category

def test_add_product_to_category():
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
    category1 = Category("Смартфоны", "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни", [product1, product2, product3])

    product4 = Product("55\" QLED 4K", "Фоновая подсветка", 123000.0, 7)
    category1.add_product(product4)
    assert "55\" QLED 4K, 123000.0 руб. Остаток: 7 шт." in category1.products
    assert category1.product_count == 4

def test_new_product():
    new_product = Product.new_product({"name": "Samsung Galaxy S23 Ultra", "description": "256GB, Серый цвет, 200MP камера", "price": 180000.0, "quantity": 5})
    assert new_product.name == "Samsung Galaxy S23 Ultra"
    assert new_product.description == "256GB, Серый цвет, 200MP камера"
    assert new_product.price == 180000.0
    assert new_product.quantity == 5

def test_set_price():
    new_product = Product("Test Product", "Test Description", 100.0, 10)
    new_product.price = 800
    assert new_product.price == 800

    with pytest.raises(ValueError):
        new_product.price = -100
    assert new_product.price == 800

    new_product.price = 0
    assert new_product.price == 0

def test_create_product_with_zero_quantity():
    with pytest.raises(ValueError) as exc_info:
        Product("Test Product", "Test Description", 100.0, 0)
    assert str(exc_info.value) == "Товар с нулевым количеством не может быть добавлен"

def test_average_product_price_with_no_products():
    category = Category("Test Category", "Test Category")
    assert category.middle_price() == 0