import logging
import os

# Log directory and file
LOG_DIR = "logs"
LOG_FILE = os.path.join(LOG_DIR, "trading_bot.log")

# Ensure log directory exists
os.makedirs(LOG_DIR, exist_ok=True)

# Basic logging configuration
logging.basicConfig(
    level=logging.INFO,                                              # INFO level captures normal flow + important events

    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
    handlers=[
        logging.FileHandler(LOG_FILE),
        logging.StreamHandler()
    ]
)

# Shared logger for the application
logger = logging.getLogger("TradingBot")
