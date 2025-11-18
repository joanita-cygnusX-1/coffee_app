# Design Document – Coffee App

## 1. Overview
This document describes how the Coffee App is structured, how data flows, and how the main features are implemented.

The goal is to keep the design simple, modular, and easy to extend.

---

## 2. Architecture
The app uses a **modular, functional structure**:

- `menu_data` → stores menu items and prices  
- `cart` → holds the user’s selected items  
- Core functions:
  - `display_menu()`
  - `get_order()`
  - `add_to_cart()`
  - `view_cart()`
  - `edit_cart()`
  - `delete_item()`
  - `calculate_total()`
  - `checkout()`

---

## 3. Data Structures

### Menu
Stored as a dictionary:
```python
menu = {
    "Latte": 12.0,
    "Cappuccino": 10.0,
    "Espresso": 8.0,
    "Mocha": 14.0
}


Cart

Stored as a list of dictionaries:

cart = [
    {"item": "Latte", "quantity": 2, "price": 12.0}
]

4. User Flow

User launches the app → sees app name

Menu loads and displays

User selects item(s)

Item added to cart

User may:

View cart

Edit quantities

Delete items

Cancel order

User proceeds to checkout

Receipt is displayed (print or go-green option)

5. Future Scaling

As the application grows, this design may include:

Splitting into modules (menu.py, cart.py, checkout.py)

Using classes instead of functions

Storing menu in a database or JSON file

Adding payment gateways (Stripe, Tap, etc.)


---

