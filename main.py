import logging
from pprint import pprint

from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State
import kbs
import requests
from bs4 import BeautifulSoup
import json
import lxml

import aiohttp
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, \
    InlineKeyboardButton, ParseMode

from aiogram.utils.markdown import text
from aiogram.dispatcher.filters import Text
from aiogram.types.base import String
from aiogram import Bot, Dispatcher, executor, types

token = '5853890770:AAGwiZYR2fOWFMCpcytF6ApoInUOO7GRmLM'
bot = Bot(token)
dp = Dispatcher(bot, storage=MemoryStorage())
ID = 0
Name = ''
class NotifyOrder(StatesGroup):
    waiting_for_msg = State()
    waiting_for_confirm = State()
# Диспетчер для бота

logging.basicConfig(level=logging.INFO)
# Включаем логирование, чтобы не пропустить важные сообщения


def cipher_caesar(s: str, n: int):
    alpha = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    s = s.lower()
    s2 = ''
    for letter in s:
        if letter in alpha:
            nomer = alpha.find(letter)
            s2 += alpha[(nomer + n) % len(alpha)]
        else:
            s2 += letter

        return s2


@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):
    global ID, Name
    ID = message.from_user.id
    Name = message.from_user.first_name

    await bot.send_message(ID, 'Какую специальность ВУЗа выбираете?', reply_markup=kbs.st_but)

@dp.callback_query_handler(text='arch')
async def arch_vuz(callback_query: types.CallbackQuery):
    await bot.send_message(callback_query.from_user.id, 'Возможно, вам стоит присмотреться к этим вузам.\nВыберите, какой из них вас интересует')

if __name__ == "__main__":
    # Запуск бота
    executor.start_polling(dp, skip_updates=True)
