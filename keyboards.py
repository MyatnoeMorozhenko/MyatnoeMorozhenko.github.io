from aiogram.types import WebAppInfo, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram import types 

kb = InlineKeyboardButton('Digital Breakfast', web_app=WebAppInfo(url = 'https://myatnoemorozhenko.github.io/'))
keyboard = InlineKeyboardMarkup().add(kb)

