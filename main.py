from aiogram import Bot, Dispatcher
from aiogram.utils import executor
import asyncio
import os
from dotenv import load_dotenv

load_dotenv()
bot = Bot(os.getenv('TOKEN'))
dp = Dispatcher(bot=bot)

HOST = "0.0.0.0"
port = 10000

async def main():
    from handlers import dp
    try:
        await dp.start_polling()
    finally:
        await bot.session.close()

if __name__ == "__main__":
    try:
        asyncio.run(main(HOST, port))
    except (KeyboardInterrupt, SystemExit):
        print('Bot stopped!')
