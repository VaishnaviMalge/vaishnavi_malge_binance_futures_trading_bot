# Basic input validation

def validate(order_type, quantity, price):
    if quantity <= 0:
        raise ValueError("Quantity must be greater than zero")

    if order_type == "LIMIT" and price is None:
        raise ValueError("Price is required for LIMIT orders")
