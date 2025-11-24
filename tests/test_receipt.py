# tests/test_receipt.py
from cart import Cart
from coffee_app import generate_receipt_text
import pytest

def test_generate_receipt_text():
    menu = [
        {"id": "1", "name": "Espresso", "price": 2.5},
        {"id": "2", "name": "Latte", "price": 3.5},
    ]
    c = Cart()
    c.add("1", 2)  # 5.0
    text, total = generate_receipt_text(c, menu, "sess1")
    assert "Espresso x 2" in text
    assert total == pytest.approx(5.0)
