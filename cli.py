import argparse
from bot.client import BinanceFuturesClient
from bot.orders import OrderService
from bot.logging_config import logger


def main():
    # CLI argument parser
    parser = argparse.ArgumentParser("Binance Futures Testnet Trading Bot")

    # Required trading parameters
    parser.add_argument("--symbol", required=True)              # e.g. BTCUSDT
    parser.add_argument("--side", required=True, choices=["BUY", "SELL"])
    parser.add_argument("--type", required=True, choices=["MARKET", "LIMIT"])
    parser.add_argument("--quantity", required=True, type=float)
    parser.add_argument("--price", type=float)                  # Only for LIMIT

    args = parser.parse_args()

    try:
        # Initialize client and order service
        client = BinanceFuturesClient()
        service = OrderService(client)

        # Print user input summary
        print("\nOrder Summary")
        print(vars(args), "\n")


        # Place order on Binance Futures Testnet
        response = service.create(
            symbol=args.symbol,
            side=args.side,
            order_type=args.type,
            quantity=args.quantity,
            price=args.price
        )

        # Print important order response details
        print("Order Successful")
        print(f"Order ID: {response.get('orderId')}")
        print(f"Status: {response.get('status')}")
        print(f"Executed Qty: {response.get('executedQty')}")
        print(f"Avg Price: {response.get('avgPrice', 'N/A')}")

    except Exception as e:
        # Log error and show clean message to user
        logger.error(e)
        print("Order Failed:", e)


if __name__ == "__main__":
    # Entry point for CLI execution
    main()
