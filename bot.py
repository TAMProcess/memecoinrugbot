import asyncio
from aiogram import executor
from handlers import dp

if __name__ == "__main__":
    # Start polling (non-stop bot loop) - skip old updates on restart
    executor.start_polling(dp, skip_updates=True)
