#!/usr/bin/env python3
# coffee_app.py
from uuid import uuid4
from menu import load_menu, display_menu, find_item
from cart import Cart
import os
from datetime import datetime

RECEIPT_DIR = "receipts"
os.makedirs(RECEIPT_DIR, exist_ok=True) 

def initialize_app():
    session_id = str(uuid4())[:8]
    menu = load_menu()
    print("=== Coffee App ===")
    print("Session ID:", session_id)
    return session_id, menu

def view_cart(cart: Cart, menu):
    if not cart.items:
        print("\nCart is empty.")
        return
    print("\n--- Your Cart ---")
    print(cart.summary(menu))
    print("-----------------")

def format_currency(value: float) -> str:
    return f"AED {value:.2f}"

def generate_receipt_text(cart, menu, session_id):
    """
    Returns a nicely formatted receipt string.
    """
    lines = []
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    lines.append("COFFEE APP RECEIPT")
    lines.append(f"Session: {session_id}")
    lines.append(f"Date: {now}")
    lines.append("-" * 28)
    total = 0.0
    price_map = {str(m["id"]): float(m["price"]) for m in menu}
    name_map = {str(m["id"]): m.get("name", str(m["id"])) for m in menu}
    for item_id, qty in cart.items.items():
        price = price_map.get(str(item_id), 0.0)
        subtotal = price * qty
        total += subtotal
        lines.append(f"{name_map.get(str(item_id),item_id)} x {qty} — {format_currency(subtotal)}")
    lines.append("-" * 28)
    lines.append(f"TOTAL: {format_currency(total)}")
    lines.append("-" * 28)
    lines.append("Payment: Simulated")
    return "\n".join(lines), total

def save_receipt_text(text, prefix="receipt"):
    ts = datetime.now().strftime("%Y%m%d%H%M%S")
    filename = os.path.join(RECEIPT_DIR, f"{prefix}_{ts}.txt")
    with open(filename, "w", encoding="utf-8") as f:
        f.write(text)
    return filename

def main():
    session_id, menu = initialize_app()
    cart = Cart()

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
            cart.add(item_id, qty)
            print(f"Added {qty} x {item['name']} to cart.")

        elif choice in ('v', 'view'):
            view_cart(cart, menu)

        elif choice in ('e', 'edit'):
            view_cart(cart, menu)
            if not cart.items:
                continue
            item_id = input("Enter item id to edit/remove: ").strip()
            if item_id not in cart.items:
                print("Item not in cart.")
                continue
            try:
                qty = int(input("Enter new quantity (0 to remove): ").strip())
            except ValueError:
                print("Invalid quantity.")
                continue
            cart.update(item_id, qty)
            print("Cart updated.")

        elif choice in ('c', 'checkout'):
            if not cart.items:
                print("Cannot checkout: cart is empty.")
                continue
            receipt_text, total = generate_receipt_text(cart, menu, session_id)
            print("\n--- Checkout ---")
            print(receipt_text)
            # Ask how to handle receipt
            print("\nOptions: (p)rint receipt (save)  (g)o green (no receipt)  (q)uit and keep session")
            action = input("Choose option: ").strip().lower()
            if action in ('p', 'print', 's', 'save'):
                path = save_receipt_text(receipt_text)
                print(f"Receipt saved to {path}")
            else:
                print("No receipt saved (Go green).")
            # simulate payment
            input("Press Enter to simulate payment...")
            print("Payment simulated. Order placed.")
            cart.clear()
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
