from binance.client import Client
from bot.logging_config import logger
import os


class BinanceFuturesClient:
    def __init__(self):
        # Read API credentials from environment variables
        api_key = os.getenv("BINANCE_API_KEY")
        api_secret = os.getenv("BINANCE_API_SECRET")

        # Stop execution if keys are missing
        if not api_key or not api_secret:
            raise ValueError("API keys not found in environment variables")

        # Initialize Binance client
        self.client = Client(api_key, api_secret)

        # Force client to use Futures Testnet
        self.client.FUTURES_URL = "https://testnet.binancefuture.com"

        logger.info("Binance Futures Testnet client initialized")

    def place_order(self, **kwargs):
        """
        Places a futures order on Binance Testnet.
        Expects order parameters like symbol, side, type, quantity, price.
        """
        try:
            # Log order request before sending
            logger.info(f"Placing order: {kwargs}")

            # Send order to Binance Futures API
            response = self.client.futures_create_order(**kwargs)

            # Log successful API response
            logger.info(f"Order response: {response}")

            return response

        except Exception as e:
            # Log API or network errors
            logger.error(f"API Error: {e}")
            raise
