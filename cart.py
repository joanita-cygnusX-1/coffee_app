# cart.py
from typing import Dict, List

class Cart:
    def __init__(self):
        """
        Initialize a new cart.
        Items stored as dict: item_id (str) -> quantity (int)
        """
        self.items: Dict[str, int] = {}

    def add(self, item_id: str, qty: int = 1) -> None:
        if qty < 1:
            return
        self.items[item_id] = self.items.get(item_id, 0) + qty

    def remove(self, item_id: str) -> None:
        self.items.pop(item_id, None)

    def update(self, item_id: str, qty: int) -> None:
        if qty <= 0:
            self.remove(item_id)
        else:
            self.items[item_id] = qty

    def clear(self) -> None:
        self.items.clear()

    def total(self, menu: List[Dict]) -> float:
        """
        Calculate total using menu (list of dicts) or dict mapping id->price.
        Accepts menu as list of dicts.
        """
        price_map = {str(m["id"]): float(m["price"]) for m in menu} if isinstance(menu, list) else dict(menu)
        return sum(price_map.get(str(item_id), 0.0) * qty for item_id, qty in self.items.items())

    def summary(self, menu: List[Dict]) -> str:
        lines: List[str] = []
        price_map = {str(m["id"]): float(m["price"]) for m in menu}
        name_map = {str(m["id"]): m["name"] for m in menu}
        for item_id, qty in self.items.items():
            name = name_map.get(str(item_id), item_id)
            price = price_map.get(str(item_id), 0.0)
            lines.append(f"{name} x {qty} = AED {price * qty:.2f}")
        lines.append(f"TOTAL: AED {self.total(menu):.2f}")
        return "\n".join(lines)
