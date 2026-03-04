

import os
from bot.client import BinanceFuturesClient
from bot.orders import OrderService
from bot.logging_config import logger

def get_input(prompt_text, choices=None, type_cast=str, required=True):
    """Helper to get validated user input"""
    while True:
        user_input = input(f"{prompt_text}: ").strip()
        if not user_input and required:
            print("This field is required.")
            continue
        if choices and user_input.upper() not in choices:
            print(f"Invalid choice. Choose from {choices}.")
            continue
        try:
            return type_cast(user_input) if user_input else None
        except ValueError:
            print(f"Invalid type. Expected {type_cast.__name__}.")

def main():
    print("=== Binance Futures Testnet Trading Bot ===\n")

    # Ask API credentials once
    api_key = os.getenv("BINANCE_API_KEY") or get_input("Enter your Binance API Key")
    api_secret = os.getenv("BINANCE_API_SECRET") or get_input("Enter your Binance API Secret")

    # Initialize client once
    client = BinanceFuturesClient(api_key=api_key, api_secret=api_secret)
    service = OrderService(client)
    print("API keys verified successfully!\n")

    # Loop to allow multiple orders in one session
    while True:
        
        symbol = get_input("Enter symbol (e.g., BTCUSDT)").upper()
        side = get_input("Enter side (BUY/SELL)", choices=["BUY", "SELL"]).upper()
        order_type = get_input("Enter order type (MARKET/LIMIT)", choices=["MARKET", "LIMIT"]).upper()
        quantity = get_input("Enter quantity", type_cast=float)
        price = None
        if order_type == "LIMIT":
            price = get_input("Enter price for LIMIT order", type_cast=float)

        # Place the order
        response = service.create(
            symbol=symbol,
            side=side,
            order_type=order_type,
            quantity=quantity,
            price=price
        )

        # Print concise response summary
        if "error" in response:
            print(f"Order failed: {response['error']}\n")
        else:
            print("\nOrder Successful!")
            print(f"Order ID: {response.get('orderId')}")
            print(f"Status: {response.get('status')}")
            print(f"Executed Qty: {response.get('executedQty')}")
            print(f"Avg Price: {response.get('avgPrice', 'N/A')}\n")

if __name__ == "__main__":
    main()
