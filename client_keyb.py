from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton

#Основное меню
b1 = InlineKeyboardButton('Меню уроков', callback_data='button1')
b2 = InlineKeyboardButton('⚙️Настройки', callback_data='button2')
b3 = InlineKeyboardButton('Помощь', url='https://t.me/testingme_supportbot')
b10 = InlineKeyboardButton('📝 Инструкция', callback_data='button5')
b11 = InlineKeyboardButton('Изменить язык', callback_data='button6')
"""News = InlineKeyboardButton('Новости', callback_data='news')"""
back_to_menu = InlineKeyboardButton('Вернуться в главное меню', callback_data='back')

"keyb_client = ReplyKeyboardMarkup(resize_keyboard=True)"


keyb_client = InlineKeyboardMarkup().add(b1).add(b10).add(b2).insert(b3)

"keyb_client.add(b3).add(b2).insert(b1)"

#Settings

keyb_client_set = InlineKeyboardMarkup().add(b11).add(back_to_menu)


#Меню уроков основное:
urok = InlineKeyboardButton('Вводный курс', callback_data='beginer')
level1 = InlineKeyboardButton('Уровень 1', callback_data='beginer1')

keyb_client_menu = InlineKeyboardMarkup().add(urok).add(level1).add(back_to_menu)

#Меню вводного курса:
urok1 = InlineKeyboardButton('Урок 1', callback_data='urok1')
urok2 = InlineKeyboardButton('Урок 2', callback_data='urok2')
urok3 = InlineKeyboardButton('Урок 3', callback_data='urok3')
urok4 = InlineKeyboardButton('Урок 4', callback_data='urok4')
urok5 = InlineKeyboardButton('Урок 5', callback_data='urok5')
back_to_back = InlineKeyboardButton('⬅️ Назад', callback_data='back_to_back')

keyb_client2 = ReplyKeyboardMarkup(resize_keyboard=True)

keyb_client2 = InlineKeyboardMarkup().add(urok1).row(urok2, urok3).insert(urok4).add(urok5).add(back_to_back)

#Меню для упражнений и граммы вводного курса:
b6 = InlineKeyboardButton('📓Словарь', url= 'https://quizlet.com/shinymeerkat/folders/korean-01?i=4ypdqj&x=1xqY' )
b_intro_1 = InlineKeyboardButton('💪Приступить к упражнениям', callback_data='b_intro_1')
b_intro_2 = InlineKeyboardButton('💪Приступить к упражнениям', callback_data='b_intro_2')
b_intro_3 = InlineKeyboardButton('💪Приступить к упражнениям', callback_data='b_intro_3')
b_intro_4 = InlineKeyboardButton('💪Приступить к упражнениям', callback_data='b_intro_4')
b_intro_5 = InlineKeyboardButton('💪Приступить к упражнениям', callback_data='b_intro_5')

b8 = InlineKeyboardButton('🎥Видео-уроки', url = 'https://quizlet.com/shinymeerkat/folders/korean-01?i=4ypdqj&x=1xqY')
b9 = InlineKeyboardButton('🔠Грамматика', url ='https://debonair-brother-8d3.notion.site/cd5b668aa4954c1e8cdf47987172c128?v=0a8c655a5bbd4180951195758984572f')
back_to_back01 = InlineKeyboardButton('⬅️ Назад', callback_data='back_to_back01')

keyb_client_intro_1 = InlineKeyboardMarkup().row(b6, b9).add(b8).add(b_intro_1).add(back_to_back01)
keyb_client_intro_2 = InlineKeyboardMarkup().row(b6, b9).add(b8).add(b_intro_2).add(back_to_back01)
keyb_client_intro_3 = InlineKeyboardMarkup().row(b6, b9).add(b8).add(b_intro_3).add(back_to_back01)
keyb_client_intro_4 = InlineKeyboardMarkup().row(b6, b9).add(b8).add(b_intro_4).add(back_to_back01)
keyb_client_intro_5 = InlineKeyboardMarkup().row(b6, b9).add(b8).add(b_intro_5).add(back_to_back01)

"""keyb_client3 = ReplyKeyboardMarkup(resize_keyboard=True)

#keyb_client3.row(b6, b9).add(b7).add(b8)"""

#Меню для первого уровня:

back_to_back_l1 = InlineKeyboardButton('⬅️ Назад', callback_data='back_to_back_l1')

keyb_client_level1_back = InlineKeyboardMarkup().row(b6, b9).add(b8).add(b_intro_1).add(back_to_back_l1)



urok_l1 = InlineKeyboardButton('Числительные в корейском языке', url = 'https://www.notion.so/3-d76051bfeb4f4eb8ae442696c65f4f7d?pvs=4')
urok_l2 = InlineKeyboardButton('Прошедшее время', url='https://www.notion.so/2-6289b2b24f7842038f991c28ba1d938e?pvs=4')


keyb_client_level1 = InlineKeyboardMarkup().add(urok_l1).add(urok_l2)


