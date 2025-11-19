#!/usr/bin/env python3
"""
coffee_app.py
Simple CLI-based coffee app MVP for learning backend concepts.
Run: python3 coffee_app.py
"""

import json
import uuid
from datetime import datetime

MENU_FILE = "menu.json"

def initialize_app():
    session_id = str(uuid.uuid4())[:8]
    menu = load_menu()
    print("=== Coffee App ===")
    print("Session ID:", session_id)
    return session_id, menu

def load_menu():
    try:
        with open(MENU_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        # Fallback sample menu if file missing
        sample = [
            {"id": "1", "name": "Espresso", "price": 2.5, "description": "Strong shot"},
            {"id": "2", "name": "Latte", "price": 3.5, "description": "Milk and coffee"},
            {"id": "3", "name": "Cappuccino", "price": 3.0, "description": "Foam top"}
        ]
        return sample

def display_menu(menu):
    print("\n--- Menu ---")
    for item in menu:
        print(f"{item['id']}. {item['name']} - AED {item['price']:.2f}  ({item.get('description','')})")
    print("------------")

def find_item(menu, item_id):
    for item in menu:
        if str(item["id"]) == str(item_id):
            return item
    return None

def add_to_cart(cart, item_id, qty):
    if item_id in cart:
        cart[item_id] += qty
    else:
        cart[item_id] = qty

def remove_from_cart(cart, item_id):
    cart.pop(item_id, None)

def update_quantity(cart, item_id, qty):
    if qty <= 0:
        remove_from_cart(cart, item_id)
    else:
        cart[item_id] = qty

def calculate_total(cart, menu):
    total = 0.0
    for item_id, qty in cart.items():
        item = find_item(menu, item_id)
        if item:
            total += item["price"] * qty
    return total

def view_cart(cart, menu):
    if not cart:
        print("\nCart is empty.")
        return
    print("\n--- Your Cart ---")
    for item_id, qty in cart.items():
        item = find_item(menu, item_id)
        if item:
            subtotal = item["price"] * qty
            print(f"{item['name']} x {qty} = AED {subtotal:.2f}")
    total = calculate_total(cart, menu)
    print(f"Total: AED {total:.2f}")
    print("-----------------")

def checkout(cart, menu, session_id):
    if not cart:
        print("Cannot checkout: cart is empty.")
        return False
    total = calculate_total(cart, menu)
    print("\n--- Checkout ---")
    print(f"Session: {session_id}")
    print(f"Total: AED {total:.2f}")
    # Mock payment here
    input("Press Enter to simulate payment...")
    order = {
        "order_id": str(uuid.uuid4())[:8],
        "session": session_id,
        "items": [{ "id": item_id, "qty": qty, "name": find_item(menu,item_id)["name"], "price": find_item(menu,item_id)["price"] } for item_id, qty in cart.items()],
        "total": total,
        "timestamp": datetime.utcnow().isoformat()
    }
    cart.clear()
    print("Payment simulated. Order placed.")
    print_receipt(order)
    return True

def print_receipt(order):
    print("\n===== RECEIPT =====")
    print(f"Order ID: {order['order_id']}")
    print(f"Session: {order['session']}")
    print(f"Time: {order['timestamp']}")
    for it in order["items"]:
        print(f"{it['name']} x {it['qty']} = AED {it['price']*it['qty']:.2f}")
    print(f"TOTAL: AED {order['total']:.2f}")
    print("===================")

def main():
    session_id, menu = initialize_app()
    cart = {}
    while True:
        display_menu(menu)
        print("\nOptions: (a)dd (v)iew cart (e)dit cart (c)heckout (q)uit")
        choice = input("Choose an option: ").strip().lower()
        if choice in ('a', 'add'):
            item_id = input("Enter item id to add: ").strip()
            item = find_item(menu, item_id)
            if not item:
                print("Invalid id.")
                continue
            try:
                qty = int(input("Enter quantity: ").strip())
            except ValueError:
                print("Invalid quantity.")
                continue
            if qty <= 0:
                print("Quantity must be >= 1")
                continue
            add_to_cart(cart, item_id, qty)
            print(f"Added {qty} x {item['name']} to cart.")
        elif choice in ('v', 'view'):
            view_cart(cart, menu)
        elif choice in ('e', 'edit'):
            view_cart(cart, menu)
            if not cart:
                continue
            item_id = input("Enter item id to edit/remove: ").strip()
            if item_id not in cart:
                print("Item not in cart.")
                continue
            try:
                qty = int(input("Enter new quantity (0 to remove): ").strip())
            except ValueError:
                print("Invalid quantity.")
                continue
            update_quantity(cart, item_id, qty)
            print("Cart updated.")
        elif choice in ('c', 'checkout'):
            success = checkout(cart, menu, session_id)
            if success:
                # after checkout, decide to quit or start new order
                again = input("Place another order? (y/n): ").strip().lower()
                if again != 'y':
                    break
        elif choice in ('q', 'quit'):
            print("Goodbye.")
            break
        else:
            print("Unknown option. Try again.")

if __name__ == "__main__":
    main()
