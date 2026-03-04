import os
from binance.client import Client
from bot.logging_config import logger


class BinanceFuturesClient:
    def __init__(self, api_key=None, api_secret=None):
        # Prefer CLI input, fallback to environment variables
        self.api_key = api_key or os.getenv("BINANCE_API_KEY")
        self.api_secret = api_secret or os.getenv("BINANCE_API_SECRET")

        if not self.api_key or not self.api_secret:
            raise ValueError(
                "Binance API credentials not provided. "
                "Use CLI arguments or environment variables."
            )

        self.client = Client(self.api_key, self.api_secret)
        self.client.FUTURES_URL = "https://testnet.binancefuture.com"

        logger.info("Binance Futures Testnet client initialized")

    def place_order(self, **order):
        try:
            logger.info(f"Order request: {order}")
            response = self.client.futures_create_order(**order)
            logger.info(f"Order response: {response}")
            return response
        except Exception as e:
            logger.error(f"API error: {e}")
            raise
