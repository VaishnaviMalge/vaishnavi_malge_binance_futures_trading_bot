# Binance Futures Testnet Trading Bot (Python)

A lightweight Python CLI application to place trades on **Binance Futures Testnet (USDT-M)**.  
Built as part of a hiring assignment with clean structure, validation, logging, and error handling.

---

## Features
- Place **MARKET** and **LIMIT** orders
- Supports **BUY** and **SELL**
- CLI-based input using `argparse`
- API credentials via CLI (optional) or environment variables (recommended)
- Structured and reusable codebase
- File-based logging of API requests, responses, and errors
- Clear success and failure output

---

## Prerequisites
- Python 3.8+
- Binance Futures **Testnet** account
- Testnet API Key & Secret

---

## Setup

- Install dependencies  
  `pip install -r requirements.txt`

- Provide Binance Futures Testnet API credentials  
  (passed via CLI when running the command or via environment variables)

- Run the application with required order parameters to place an order  
  `python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001`

- Application places the order and automatically saves logs to  
  `logs/trading_bot.log`
