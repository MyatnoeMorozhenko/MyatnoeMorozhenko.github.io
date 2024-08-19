from aiogram.types import WebAppInfo, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram import types 

web_app = WebAppInfo(url='https://myatnoemorozhenko.github.io/')

keyboard = types.InlineKeyboardMarkup(
    keyboard=[
        [types.InlineKeyboardButton(text='Digital Breakfast', web_app=web_app)]
    ]
)

