from aiogram import Bot, Dispatcher
from aiogram.utils import executor
import asyncio
import os
from dotenv import load_dotenv
from handlers import dp

load_dotenv()
bot = Bot(os.getenv('TOKEN'))
dp = Dispatcher(bot=bot)

@dp.message_handler(commands=['start'])
async def start(msg: types.Message):
    user_id = msg.from_user.id
    username = msg.from_user.username
    await bot.send_photo(msg.from_user.id, caption = f"Добрый день, {msg.from_user.full_name}\!\n\nНажимай на кнопку и смотри меню Digital завтрака!",
                         parse_mode='MarkdownV2'
                         reply_markup=keyb_client)

if __name__ == "__main__":
    try:
        executor.start_polling(dp, skip_updates=True)
    except (KeyboardInterrupt, SystemExit):
        print('Bot stopped!')
