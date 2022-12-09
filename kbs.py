from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, \
    InlineKeyboardButton
import unicodedata

nokb = ReplyKeyboardRemove()

btn1 = InlineKeyboardButton('Архитектура и строительство', callback_data='arch')
btn2 = InlineKeyboardButton('Военное дело, безопасность, охрана', callback_data='mil')
btn3 = InlineKeyboardButton('Дипломатия', callback_data='dip')
btn4 = InlineKeyboardButton('Лингвистика', callback_data='ling')
btn5 = InlineKeyboardButton('IT', callback_data='it')
btn6 = InlineKeyboardButton('Искусство', callback_data='pnt')
btn7 = InlineKeyboardButton('Спорт', callback_data='pe')
btn8 = InlineKeyboardButton('Медицина', callback_data='med')
btn9 = InlineKeyboardButton('Инженерные технологии', callback_data='eng')
btn10 = InlineKeyboardButton('Химико-биологические науки', callback_data='chem')
st_but = InlineKeyboardMarkup(row_width=3)
st_but.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9, btn10)
