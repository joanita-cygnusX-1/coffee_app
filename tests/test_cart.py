import pytest
from cart import Cart

def test_add_and_total():
    menu = [
        {"id": "1", "name": "Espresso", "price": 2.5},
        {"id": "2", "name": "Latte", "price": 3.5},
    ]
    c = Cart()
    c.add("1", 2)
    c.add("2", 1)
    assert c.total(menu) == pytest.approx(8.5)
