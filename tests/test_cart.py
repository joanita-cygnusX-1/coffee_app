# tests/test_cart.py
from cart import Cart

def test_add_and_total():
    menu = [
        {"id": "1", "name": "Espresso", "price": 2.5},
        {"id": "2", "name": "Latte", "price": 3.5},
    ]
    c = Cart()
    c.add("1", 2)   # 2 * 2.5 = 5.0
    c.add("2", 1)   # 1 * 3.5 = 3.5
    assert c.total(menu) == pytest.approx(8.5)

