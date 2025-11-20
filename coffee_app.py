#!/usr/bin/env python3
# coffee_app.py
from uuid import uuid4
from menu import load_menu, display_menu, find_item
from cart import Cart

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
            print("\n--- Checkout ---")
            print(cart.summary(menu))
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
