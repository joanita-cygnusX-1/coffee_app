# menu.py
import json
from typing import List, Dict, Optional

MENU_FILE = "menu.json"

def load_menu() -> List[Dict]:
    """
    Load menu from menu.json. If file not found, return a small sample menu.
    Returns a list of dicts with keys: id, name, price, description
    """
    try:
        with open(MENU_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        # fallback sample menu
        return [
            {"id": "1", "name": "Espresso", "price": 2.5, "description": "Strong black coffee"},
            {"id": "2", "name": "Latte", "price": 3.5, "description": "Smooth milk coffee"},
            {"id": "3", "name": "Cappuccino", "price": 3.0, "description": "Frothy and strong"}
        ]

def display_menu(menu: List[Dict]) -> None:
    """Print the menu with nicely formatted prices"""
    print("\n--- MENU ---")
    for item in menu:
        print(f"{item['id']}. {item['name']} — AED {item['price']:.2f}")
        if item.get("description"):
            print(f"    {item['description']}")
    print("------------")

def find_item(menu: List[Dict], item_id: str) -> Optional[Dict]:
    """Return the menu item dict that matches item_id or None"""
    for item in menu:
        if str(item.get("id")) == str(item_id):
            return item
    return None

def menu_to_price_map(menu: List[Dict]) -> Dict[str, float]:
    """Return a mapping of id -> price (helpful for Cart.total)"""
    return {str(item["id"]): float(item["price"]) for item in menu}
