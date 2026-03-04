from bot.validators import validate


class OrderService:
    def __init__(self, client):
        # Inject Binance client dependency
        self.client = client

    def create(self, symbol, side, order_type, quantity, price=None):
        # Validate basic order inputs before API call
        validate(order_type, quantity, price)

        # Base order payload
        order = {
            "symbol": symbol,
            "side": side,
            "type": order_type,
            "quantity": quantity
        }

        # LIMIT orders require price and timeInForce
        if order_type == "LIMIT":
            order.update({
                "price": price,
                "timeInForce": "GTC"
            })

        # Forward order to Binance client
        return self.client.place_order(**order)
