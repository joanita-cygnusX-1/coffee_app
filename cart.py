# cart.py
class Cart:
    def __init__(self):
        """
        Initialize a new cart.
        We store items as a dict mapping item_id (str) -> quantity (int).
        """
        self.items = {}

    def add(self, item_id, qty=1):
        if qty < 1:
            return
        self.items[item_id] = self.items.get(item_id, 0) + qty

    def remove(self, item_id):
        self.items.pop(item_id, None)

    def update(self, item_id, qty):
        if qty <= 0:
            self.remove(item_id)
        else:
            self.items[item_id] = qty

    def clear(self):
        self.items.clear()

    def total(self, menu):
        """menu is a list of dicts or dict mapping id->item"""
        # if menu is list of dicts, convert to id->price
        price_map = {}
        if isinstance(menu, list):
            for m in menu:
                price_map[str(m["id"])] = m["price"]
        else:
            # assume dict mapping item->price
            price_map = {k: v for k, v in menu.items()}

        return sum(price_map.get(str(item_id), 0) * qty for item_id, qty in self.items.items())

    def summary(self, menu):
        lines = []
        for item_id, qty in self.items.items():
            name = next((m["name"] for m in menu if str(m["id"]) == str(item_id)), item_id)
            price = next((m["price"] for m in menu if str(m["id"]) == str(item_id)), 0)
            lines.append(f"{name} x {qty} = AED {price*qty:.2f}")
        lines.append(f"TOTAL: AED {self.total(menu):.2f}")
        return "\n".join(lines)
