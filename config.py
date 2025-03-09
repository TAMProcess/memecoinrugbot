import os
from dotenv import load_dotenv

# Load environment variables from a .env file (if present)
load_dotenv()

# Bot token from environment (required)
BOT_TOKEN = os.getenv("BOT_TOKEN")
if not BOT_TOKEN:
    raise EnvironmentError("BOT_TOKEN is not set. Please define it in a .env file or environment variable.")

# Static Solana payment address (could also be set in .env for convenience)
SOL_ADDRESS = os.getenv("SOL_ADDRESS", "SOLANA_WALLET_ADDRESS_HERE")
