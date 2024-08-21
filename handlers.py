from main import bot, dp
from keyboards import keyboard
from aiogram import types
from aiogram.dispatcher.filters import Command
import psycopg2

DB_URL = 'postgresql://postgres:FRQlnZKVGPgRvCSUcZaDfYlqWZtUpsJd@junction.proxy.rlwy.net:10150/railway'
pay_token = '1744374395:TEST:c172bfd1a3258f663519'

### To connect with DATABASE
db = psycopg2.connect(DB_URL, sslmode='require')
db_object = db.cursor()

@dp.message_handler(Command('start'))
async def start(message: types.Message):
    await bot.send_message(message.chat.id, 'Жми на кнопку и выбирай свой digital breakfast \U0001F373',
                           reply_markup=keyboard)


PRICE = {
    '1': [types.LabeledPrice(label='Английский завтрак', amount=100000)],
    '2': [types.LabeledPrice(label='Бутерброд по-македонски', amount=70000)],
    '3': [types.LabeledPrice(label='Йогурт с Яной', amount=65000)],
    '4': [types.LabeledPrice(label='Комбо: Mindbox + колла от Мартина', amount=20000)],
    '5': [types.LabeledPrice(label='Комбо: Вебинар + Кофе', amount=20000)],
    '6': [types.LabeledPrice(label='Комбо: Jira + зелёный чай', amount=15000)]
}

PRODUCT = {
    '1': [types.Invoice(title='Английский завтрак')],
    '2': [types.Invoice(title='Бутерброд по-македонски')],
    '3': [types.Invoice(title='Йогурт с Яной')],
    '4': [types.Invoice(title='Комбо: Mindbox + колла от Мартина')],
    '5': [types.Invoice(title='Комбо: Вебинар + Кофе')],
    '6': [types.Invoice(titlel='Комбо: Jira + зелёный чай')]
}

@dp.message_handler(content_types='web_app_data')
async def buy_process(web_app_message):
    await bot.send_invoice(web_app_message.chat.id,
                           title='Digital Breakfast',
                           description='Завтрак с Connect',
                           provider_token= pay_token,
                           currency='rub',
                           prices=PRICE[f'{web_app_message.web_app_data.data}'],
                           start_parameter='example',
                           payload='some_invoice')
  #коннект с бд   
    user_id = message.from_user.id
    username = message.from_user.username
    price = PRICE[f'{web_app_message.web_app_data.data}']
    product = PRODUCT[f'{web_app_message.web_app_data.data}']
    
    db_object.execute(f"SELECT id FROM users WHERE id = {user_id}")
    result = db_object.fetchone()
    
    if not result:
        db_object.execute("INSERT INTO users (id, username, price, product) VALUES (%s, %s, %s, %s)", (user_id, username, price, product))
        db.commit()

@dp.pre_checkout_query_handler(lambda query: True)
async def pre_checkout_process(pre_checkout: types.PreCheckoutQuery):
    await bot.answer_pre_checkout_query(pre_checkout.id, ok=True)

@dp.message_handler(content_types=types.ContentType.SUCCESSFUL_PAYMENT)
async def successful_payment(message: types.Message):
    await bot.send_message(message.chat.id, 'Платеж прошел успешно!')
