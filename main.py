import asyncio
import copy
import logging
import emoji
from pprint import pprint
import sqlite3
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State
import kbs
import requests
from bs4 import BeautifulSoup
import json

import aiohttp
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, \
    InlineKeyboardButton, ParseMode

from aiogram.utils.markdown import text
from aiogram.dispatcher.filters import Text
from aiogram.types.base import String
from aiogram import Bot, Dispatcher, executor, types


# -----------------------------------------------------

token = '5853890770:AAGwiZYR2fOWFMCpcytF6ApoInUOO7GRmLM'
bot = Bot(token)
dp = Dispatcher(bot, storage=MemoryStorage())
# Объект бота
# ---

cou = 0
ID = 0
Name = ''
skills = []
# Переменные
# ---

class NotifyOrder(StatesGroup):
    waiting_for_msg = State()
    waiting_for_confirm = State()
# Диспетчер для бота

logging.basicConfig(level=logging.INFO)
# Включаем логирование
# -----------------------------------------------------

@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):

    global ID, Name
    ID = message.from_user.id
    Name = message.from_user.first_name

    msg_text = f'Здравствуйте, {Name}, для начала, чтобы наши советы были более персонализированными, просим ответить на пару вопросов.'
    await bot.send_message(ID, msg_text)
    await asyncio.sleep(1)

    msg_text = 'Как по шкале от 0 до 10 вы оцените своё критическое мышление?'
    await bot.send_message(ID, msg_text)


    @dp.message_handler()
    async def crit(message: types.Message):
        global cou, skills, ID, Name
        while cou < 5:
            if int(message.text) > 10 or int(message.text) < 0:
                x = 1 / 0
            if cou < 5:
                skills.append(int(message.text))
                if cou == 0:
                    msg_text = 'Как по шкале от 0 до 10 вы оцените свою физическсую подготовку?'
                    await bot.send_message(ID, msg_text)
                elif cou == 1:
                    msg_text = 'Как по шкале от 0 до 10 вы оцените свою креативность?'
                    await bot.send_message(ID, msg_text)
                elif cou == 2:
                    msg_text = 'Как по шкале от 0 до 10 вы оцените свою эмоциональную устойчивость?'
                    await bot.send_message(ID, msg_text)
                elif cou == 3:
                    msg_text = 'Как по шкале от 0 до 10 вы оцените своё трудолюбие?'
                    await bot.send_message(ID, msg_text)
                elif cou == 4:
                    await asyncio.sleep(1)
                    await bot.send_message(ID, 'Какую специальность ВУЗа выбираете?', reply_markup=kbs.st_but)
                    # Подключение к БД
                    con = sqlite3.connect("SKIILS.db")
                    # Создание курсора
                    cur = con.cursor()
                    # print(skills)
                    print(str(ID), str(skills))
                    count = cur.execute(f"""INSERT INTO forids(Id, Skills) VALUES('{str(ID)}', '{str(skills)}')""")
                    con.commit()
                    cur.close()
                cou += 1
            print(skills)
            break



# Запуск бота
# -----------------------------------------------------

@dp.callback_query_handler(text='menu')
async def arch_vuz(callback_query: types.CallbackQuery):
    await bot.send_message(callback_query.from_user.id, 'Какую специальность ВУЗа выбираете?', reply_markup=kbs.st_but)

# Выбор специальности
# -----------------------------------------------------
@dp.callback_query_handler(text='arch')
async def arch_vuz(callback_query: types.CallbackQuery):
    await bot.send_message(callback_query.from_user.id, 'Возможно, вам стоит присмотреться к этим вузам.\nВыберите, какой из них вас интересует', reply_markup=kbs.arch_but)

@dp.callback_query_handler(text='dip')
async def arch_vuz(callback_query: types.CallbackQuery):
    await bot.send_message(callback_query.from_user.id, 'Возможно, вам стоит присмотреться к этим вузам.\nВыберите, какой из них вас интересует', reply_markup=kbs.dip_but)

@dp.callback_query_handler(text='mil')
async def arch_vuz(callback_query: types.CallbackQuery):
    await bot.send_message(callback_query.from_user.id, 'Возможно, вам стоит присмотреться к этим вузам.\nВыберите, какой из них вас интересует', reply_markup=kbs.mil_but)

@dp.callback_query_handler(text='ling')
async def arch_vuz(callback_query: types.CallbackQuery):
    await bot.send_message(callback_query.from_user.id, 'Возможно, вам стоит присмотреться к этим вузам.\nВыберите, какой из них вас интересует', reply_markup=kbs.ling_but)

@dp.callback_query_handler(text='it')
async def arch_vuz(callback_query: types.CallbackQuery):
    await bot.send_message(callback_query.from_user.id, 'Возможно, вам стоит присмотреться к этим вузам.\nВыберите, какой из них вас интересует', reply_markup=kbs.it_but)

@dp.callback_query_handler(text='pnt')
async def arch_vuz(callback_query: types.CallbackQuery):
    await bot.send_message(callback_query.from_user.id, 'Возможно, вам стоит присмотреться к этим вузам.\nВыберите, какой из них вас интересует', reply_markup=kbs.pnt_but)

@dp.callback_query_handler(text='pe')
async def arch_vuz(callback_query: types.CallbackQuery):
    await bot.send_message(callback_query.from_user.id, 'Возможно, вам стоит присмотреться к этим вузам.\nВыберите, какой из них вас интересует', reply_markup=kbs.pe_but)

@dp.callback_query_handler(text='med')
async def arch_vuz(callback_query: types.CallbackQuery):
    await bot.send_message(callback_query.from_user.id, 'Возможно, вам стоит присмотреться к этим вузам.\nВыберите, какой из них вас интересует', reply_markup=kbs.med_but)

@dp.callback_query_handler(text='chem')
async def arch_vuz(callback_query: types.CallbackQuery):
    await bot.send_message(callback_query.from_user.id, 'Возможно, вам стоит присмотреться к этим вузам.\nВыберите, какой из них вас интересует', reply_markup=kbs.chem_but)

@dp.callback_query_handler(text='eng')
async def arch_vuz(callback_query: types.CallbackQuery):
    await bot.send_message(callback_query.from_user.id, 'Возможно, вам стоит присмотреться к этим вузам.\nВыберите, какой из них вас интересует', reply_markup=kbs.eng_but)


# Вывод вузов
# -----------------------------------------------------
@dp.callback_query_handler(text='V1')
async def vz1(callback_query: types.CallbackQuery):
    global skills
    ls = copy.deepcopy(kbs.VUZ1)
    name = ls.pop(0)
    ls.pop(0)
    spisok = []
    flag = 0
    for activity in ls:
        for i in range(5):
            if skills[i] >= activity[2][i]:
                flag += 1
            else:
                flag = 0
        if flag == 5:
            spisok.append(activity[0:2])
        flag = 0

    if len(spisok) != 0:
        msg_text = f'Дополнительне баллы в {name} даются за:'
        await bot.send_message(callback_query.from_user.id, msg_text)
        for i in spisok:
            await asyncio.sleep(2)
            msg_text = f'{i[0].capitalize()} - вы получите до {i[1]} баллов.'
            await bot.send_message(callback_query.from_user.id, msg_text)
    else:
        await asyncio.sleep(2)
        msg_text = f'Извините, но мы не можем вам ничего посоветовать'
        await bot.send_message(callback_query.from_user.id, msg_text)


@dp.callback_query_handler(text='V2')
async def vz2(callback_query: types.CallbackQuery):
    global skills
    ls = copy.deepcopy(kbs.VUZ2)
    name = ls.pop(0)
    ls.pop(0)
    spisok = []
    flag = 0
    for activity in ls:
        for i in range(5):
            if skills[i] >= activity[2][i]:
                flag += 1
            else:
                flag = 0
        if flag == 5:
            spisok.append(activity[0:2])
        flag = 0

    if len(spisok) != 0:
        msg_text = f'Дополнительне баллы в {name} даются за:'
        await bot.send_message(callback_query.from_user.id, msg_text)
        for i in spisok:
            await asyncio.sleep(2)
            msg_text = f'{i[0].capitalize()} - вы получите до {i[1]} баллов.'
            await bot.send_message(callback_query.from_user.id, msg_text)
    else:
        await asyncio.sleep(2)
        msg_text = f'Извините, но мы не можем вам ничего посоветовать'
        await bot.send_message(callback_query.from_user.id, msg_text)

    # V2 вуза
    # -----------------------------------------------------

@dp.callback_query_handler(text='V3')
async def vz3(callback_query: types.CallbackQuery):
    global skills
    ls = copy.deepcopy(kbs.VUZ3)
    name = ls.pop(0)
    ls.pop(0)
    spisok = []
    flag = 0
    for activity in ls:
        for i in range(5):
            if skills[i] >= activity[2][i]:
                flag += 1
            else:
                flag = 0
        if flag == 5:
            spisok.append(activity[0:2])
        flag = 0

    if len(spisok) != 0:
        msg_text = f'Дополнительне баллы в {name} даются за:'
        await bot.send_message(callback_query.from_user.id, msg_text)
        for i in spisok:
            await asyncio.sleep(2)
            msg_text = f'{i[0].capitalize()} - вы получите до {i[1]} баллов.'
            await bot.send_message(callback_query.from_user.id, msg_text)
    else:
        await asyncio.sleep(2)
        msg_text = f'Извините, но мы не можем вам ничего посоветовать'
        await bot.send_message(callback_query.from_user.id, msg_text)

    # V3 вуза
    # -----------------------------------------------------

@dp.callback_query_handler(text='V4')
async def vz4(callback_query: types.CallbackQuery):
    global skills
    ls = copy.deepcopy(kbs.VUZ4)
    name = ls.pop(0)
    ls.pop(0)
    spisok = []
    flag = 0
    for activity in ls:
        for i in range(5):
            if skills[i] >= activity[2][i]:
                flag += 1
            else:
                flag = 0
        if flag == 5:
            spisok.append(activity[0:2])
        flag = 0


    if len(spisok) != 0:
        msg_text = f'Дополнительне баллы в {name} даются за:'
        await bot.send_message(callback_query.from_user.id, msg_text)
        for i in spisok:
            await asyncio.sleep(2)
            msg_text = f'{i[0].capitalize()} - вы получите до {i[1]} баллов.'
            await bot.send_message(callback_query.from_user.id, msg_text)
    else:
        await asyncio.sleep(2)
        msg_text = f'Извините, но мы не можем вам ничего посоветовать'
        await bot.send_message(callback_query.from_user.id, msg_text)

    # V4 вуза
    # -----------------------------------------------------

@dp.callback_query_handler(text='V5')
async def vz5(callback_query: types.CallbackQuery):
    global skills
    ls = copy.deepcopy(kbs.VUZ5)
    name = ls.pop(0)
    ls.pop(0)
    spisok = []
    flag = 0
    for activity in ls:
        for i in range(5):
            if skills[i] >= activity[2][i]:
                flag += 1
            else:
                flag = 0
        if flag == 5:
            spisok.append(activity[0:2])
        flag = 0


    if len(spisok) != 0:
        msg_text = f'Дополнительне баллы в {name} даются за:'
        await bot.send_message(callback_query.from_user.id, msg_text)
        for i in spisok:
            await asyncio.sleep(2)
            msg_text = f'{i[0].capitalize()} - вы получите до {i[1]} баллов.'
            await bot.send_message(callback_query.from_user.id, msg_text)
    else:
        await asyncio.sleep(2)
        msg_text = f'Извините, но мы не можем вам ничего посоветовать'
        await bot.send_message(callback_query.from_user.id, msg_text)
    # V5 вуза
    # -----------------------------------------------------

@dp.callback_query_handler(text='V6')
async def vz6(callback_query: types.CallbackQuery):
    global skills
    ls = copy.deepcopy(kbs.VUZ6)
    name = ls.pop(0)
    ls.pop(0)
    spisok = []
    flag = 0
    for activity in ls:
        for i in range(5):
            if skills[i] >= activity[2][i]:
                flag += 1
            else:
                flag = 0
        if flag == 5:
            spisok.append(activity[0:2])
        flag = 0

        if len(spisok) != 0:
            msg_text = f'Дополнительне баллы в {name} даются за:'
            await bot.send_message(callback_query.from_user.id, msg_text)
            for i in spisok:
                await asyncio.sleep(2)
                msg_text = f'{i[0].capitalize()} - вы получите до {i[1]} баллов.'
                await bot.send_message(callback_query.from_user.id, msg_text)
        else:
            await asyncio.sleep(2)
            msg_text = f'Извините, но мы не можем вам ничего посоветовать'
            await bot.send_message(callback_query.from_user.id, msg_text)

    # V6 вуза
    # -----------------------------------------------------

@dp.callback_query_handler(text='V7')
async def vz7(callback_query: types.CallbackQuery):
    global skills
    ls = copy.deepcopy(kbs.VUZ7)
    name = ls.pop(0)
    ls.pop(0)
    spisok = []
    flag = 0
    for activity in ls:
        for i in range(5):
            if skills[i] >= activity[2][i]:
                flag += 1
            else:
                flag = 0
        if flag == 5:
            spisok.append(activity[0:2])
        flag = 0


    if len(spisok) != 0:
        msg_text = f'Дополнительне баллы в {name} даются за:'
        await bot.send_message(callback_query.from_user.id, msg_text)
        for i in spisok:
            await asyncio.sleep(2)
            msg_text = f'{i[0].capitalize()} - вы получите до {i[1]} баллов.'
            await bot.send_message(callback_query.from_user.id, msg_text)
    else:
        await asyncio.sleep(2)
        msg_text = f'Извините, но мы не можем вам ничего посоветовать'
        await bot.send_message(callback_query.from_user.id, msg_text)

    # V7 вуза
    # -----------------------------------------------------

@dp.callback_query_handler(text='V8')
async def vz8(callback_query: types.CallbackQuery):
    global skills
    ls = copy.deepcopy(kbs.VUZ8)
    name = ls.pop(0)
    ls.pop(0)
    spisok = []
    flag = 0
    for activity in ls:
        for i in range(5):
            if skills[i] >= activity[2][i]:
                flag += 1
            else:
                flag = 0
        if flag == 5:
            spisok.append(activity[0:2])
        flag = 0


    if len(spisok) != 0:
        msg_text = f'Дополнительне баллы в {name} даются за:'
        await bot.send_message(callback_query.from_user.id, msg_text)
        for i in spisok:
            await asyncio.sleep(2)
            msg_text = f'{i[0].capitalize()} - вы получите до {i[1]} баллов.'
            await bot.send_message(callback_query.from_user.id, msg_text)
    else:
        await asyncio.sleep(2)
        msg_text = f'Извините, но мы не можем вам ничего посоветовать'
        await bot.send_message(callback_query.from_user.id, msg_text)

    # V8 вуза
    # -----------------------------------------------------

@dp.callback_query_handler(text='V9')
async def vz9(callback_query: types.CallbackQuery):
    global skills
    ls = copy.deepcopy(kbs.VUZ9)
    name = ls.pop(0)
    ls.pop(0)
    spisok = []
    flag = 0
    for activity in ls:
        for i in range(5):
            if skills[i] >= activity[2][i]:
                flag += 1
            else:
                flag = 0
        if flag == 5:
            spisok.append(activity[0:2])
        flag = 0

    if len(spisok) != 0:
        msg_text = f'Дополнительне баллы в {name} даются за:'
        await bot.send_message(callback_query.from_user.id, msg_text)
        for i in spisok:
            await asyncio.sleep(2)
            msg_text = f'{i[0].capitalize()} - вы получите до {i[1]} баллов.'
            await bot.send_message(callback_query.from_user.id, msg_text)
    else:
        await asyncio.sleep(2)
        msg_text = f'Извините, но мы не можем вам ничего посоветовать'
        await bot.send_message(callback_query.from_user.id, msg_text)

    # V9 вуза
    # -----------------------------------------------------

@dp.callback_query_handler(text='V10')
async def vz10(callback_query: types.CallbackQuery):
    global skills
    ls = copy.deepcopy(kbs.VUZ10)
    name = ls.pop(0)
    ls.pop(0)
    spisok = []
    flag = 0
    for activity in ls:
        for i in range(5):
            if skills[i] >= activity[2][i]:
                flag += 1
            else:
                flag = 0
        if flag == 5:
            spisok.append(activity[0:2])
        flag = 0

    if len(spisok) != 0:
        msg_text = f'Дополнительне баллы в {name} даются за:'
        await bot.send_message(callback_query.from_user.id, msg_text)
        for i in spisok:
            await asyncio.sleep(2)
            msg_text = f'{i[0].capitalize()} - вы получите до {i[1]} баллов.'
            await bot.send_message(callback_query.from_user.id, msg_text)
    else:
        await asyncio.sleep(2)
        msg_text = f'Извините, но мы не можем вам ничего посоветовать'
        await bot.send_message(callback_query.from_user.id, msg_text)

    # V10 вуза
    # -----------------------------------------------------

@dp.callback_query_handler(text='V11')
async def vz11(callback_query: types.CallbackQuery):
    global skills
    ls = copy.deepcopy(kbs.VUZ11)
    name = ls.pop(0)
    ls.pop(0)
    spisok = []
    flag = 0
    for activity in ls:
        for i in range(5):
            if skills[i] >= activity[2][i]:
                flag += 1
            else:
                flag = 0
        if flag == 5:
            spisok.append(activity[0:2])
        flag = 0

    if len(spisok) != 0:
        msg_text = f'Дополнительне баллы в {name} даются за:'
        await bot.send_message(callback_query.from_user.id, msg_text)
        for i in spisok:
            await asyncio.sleep(2)
            msg_text = f'{i[0].capitalize()} - вы получите до {i[1]} баллов.'
            await bot.send_message(callback_query.from_user.id, msg_text)
    else:
        await asyncio.sleep(2)
        msg_text = f'Извините, но мы не можем вам ничего посоветовать'
        await bot.send_message(callback_query.from_user.id, msg_text)

    # V11 вуза
    # -----------------------------------------------------

@dp.callback_query_handler(text='V12')
async def vz12(callback_query: types.CallbackQuery):
    global skills
    ls = copy.deepcopy(kbs.VUZ12)
    name = ls.pop(0)
    ls.pop(0)
    spisok = []
    flag = 0
    for activity in ls:
        for i in range(5):
            if skills[i] >= activity[2][i]:
                flag += 1
            else:
                flag = 0
        if flag == 5:
            spisok.append(activity[0:2])
        flag = 0

    if len(spisok) != 0:
        msg_text = f'Дополнительне баллы в {name} даются за:'
        await bot.send_message(callback_query.from_user.id, msg_text)
        for i in spisok:
            await asyncio.sleep(2)
            msg_text = f'{i[0].capitalize()} - вы получите до {i[1]} баллов.'
            await bot.send_message(callback_query.from_user.id, msg_text)
    else:
        await asyncio.sleep(2)
        msg_text = f'Извините, но мы не можем вам ничего посоветовать'
        await bot.send_message(callback_query.from_user.id, msg_text)

    # V12 вуза
    # -----------------------------------------------------

@dp.callback_query_handler(text='V13')
async def vz13(callback_query: types.CallbackQuery):
    global skills
    ls = copy.deepcopy(kbs.VUZ13)
    name = ls.pop(0)
    ls.pop(0)
    spisok = []
    flag = 0
    for activity in ls:
        for i in range(5):
            if skills[i] >= activity[2][i]:
                flag += 1
            else:
                flag = 0
        if flag == 5:
            spisok.append(activity[0:2])
        flag = 0

    if len(spisok) != 0:
        msg_text = f'Дополнительне баллы в {name} даются за:'
        await bot.send_message(callback_query.from_user.id, msg_text)
        for i in spisok:
            await asyncio.sleep(2)
            msg_text = f'{i[0].capitalize()} - вы получите до {i[1]} баллов.'
            await bot.send_message(callback_query.from_user.id, msg_text)
    else:
        await asyncio.sleep(2)
        msg_text = f'Извините, но мы не можем вам ничего посоветовать'
        await bot.send_message(callback_query.from_user.id, msg_text)

@dp.callback_query_handler(text='V14')
async def vz14(callback_query: types.CallbackQuery):
    global skills
    ls = copy.deepcopy(kbs.VUZ14)
    name = ls.pop(0)
    ls.pop(0)
    spisok = []
    flag = 0
    for activity in ls:
        for i in range(5):
            if skills[i] >= activity[2][i]:
                flag += 1
            else:
                flag = 0
        if flag == 5:
            spisok.append(activity[0:2])
        flag = 0

    if len(spisok) != 0:
        msg_text = f'Дополнительне баллы в {name} даются за:'
        await bot.send_message(callback_query.from_user.id, msg_text)
        for i in spisok:
            await asyncio.sleep(2)
            msg_text = f'{i[0].capitalize()} - вы получите до {i[1]} баллов.'
            await bot.send_message(callback_query.from_user.id, msg_text)
    else:
        await asyncio.sleep(2)
        msg_text = f'Извините, но мы не можем вам ничего посоветовать'
        await bot.send_message(callback_query.from_user.id, msg_text)

@dp.callback_query_handler(text='V15')
async def vz15(callback_query: types.CallbackQuery):
    global skills
    ls = copy.deepcopy(kbs.VUZ15)
    name = ls.pop(0)
    ls.pop(0)
    spisok = []
    flag = 0
    for activity in ls:
        for i in range(5):
            if skills[i] >= activity[2][i]:
                flag += 1
            else:
                flag = 0
        if flag == 5:
            spisok.append(activity[0:2])
        flag = 0

    if len(spisok) != 0:
        msg_text = f'Дополнительне баллы в {name} даются за:'
        await bot.send_message(callback_query.from_user.id, msg_text)
        for i in spisok:
            await asyncio.sleep(2)
            msg_text = f'{i[0].capitalize()} - вы получите до {i[1]} баллов.'
            await bot.send_message(callback_query.from_user.id, msg_text)
    else:
        await asyncio.sleep(2)
        msg_text = f'Извините, но мы не можем вам ничего посоветовать'
        await bot.send_message(callback_query.from_user.id, msg_text)

@dp.callback_query_handler(text='V16')
async def vz16(callback_query: types.CallbackQuery):
    global skills
    ls = copy.deepcopy(kbs.VUZ16)
    name = ls.pop(0)
    ls.pop(0)
    spisok = []
    flag = 0
    for activity in ls:
        for i in range(5):
            if skills[i] >= activity[2][i]:
                flag += 1
            else:
                flag = 0
        if flag == 5:
            spisok.append(activity[0:2])
        flag = 0

    if len(spisok) != 0:
        msg_text = f'Дополнительне баллы в {name} даются за:'
        await bot.send_message(callback_query.from_user.id, msg_text)
        for i in spisok:
            await asyncio.sleep(2)
            msg_text = f'{i[0].capitalize()} - вы получите до {i[1]} баллов.'
            await bot.send_message(callback_query.from_user.id, msg_text)
    else:
        await asyncio.sleep(2)
        msg_text = f'Извините, но мы не можем вам ничего посоветовать'
        await bot.send_message(callback_query.from_user.id, msg_text)

@dp.callback_query_handler(text='V17')
async def vz17(callback_query: types.CallbackQuery):
    global skills
    ls = copy.deepcopy(kbs.VUZ17)
    name = ls.pop(0)
    ls.pop(0)
    spisok = []
    flag = 0
    for activity in ls:
        for i in range(5):
            if skills[i] >= activity[2][i]:
                flag += 1
            else:
                flag = 0
        if flag == 5:
            spisok.append(activity[0:2])
        flag = 0

    if len(spisok) != 0:
        msg_text = f'Дополнительне баллы в {name} даются за:'
        await bot.send_message(callback_query.from_user.id, msg_text)
        for i in spisok:
            await asyncio.sleep(2)
            msg_text = f'{i[0].capitalize()} - вы получите до {i[1]} баллов.'
            await bot.send_message(callback_query.from_user.id, msg_text)
    else:
        await asyncio.sleep(2)
        msg_text = f'Извините, но мы не можем вам ничего посоветовать'
        await bot.send_message(callback_query.from_user.id, msg_text)

@dp.callback_query_handler(text='V18')
async def vz18(callback_query: types.CallbackQuery):
    global skills
    ls = copy.deepcopy(kbs.VUZ18)
    name = ls.pop(0)
    ls.pop(0)
    spisok = []
    flag = 0
    for activity in ls:
        for i in range(5):
            if skills[i] >= activity[2][i]:
                flag += 1
            else:
                flag = 0
        if flag == 5:
            spisok.append(activity[0:2])
        flag = 0

    if len(spisok) != 0:
        msg_text = f'Дополнительне баллы в {name} даются за:'
        await bot.send_message(callback_query.from_user.id, msg_text)
        for i in spisok:
            await asyncio.sleep(2)
            msg_text = f'{i[0].capitalize()} - вы получите до {i[1]} баллов.'
            await bot.send_message(callback_query.from_user.id, msg_text)
    else:
        await asyncio.sleep(2)
        msg_text = f'Извините, но мы не можем вам ничего посоветовать'
        await bot.send_message(callback_query.from_user.id, msg_text)

@dp.callback_query_handler(text='V19')
async def vz19(callback_query: types.CallbackQuery):
    global skills
    ls = copy.deepcopy(kbs.VUZ19)
    name = ls.pop(0)
    ls.pop(0)
    spisok = []
    flag = 0
    for activity in ls:
        for i in range(5):
            if skills[i] >= activity[2][i]:
                flag += 1
            else:
                flag = 0
        if flag == 5:
            spisok.append(activity[0:2])
        flag = 0

    if len(spisok) != 0:
        msg_text = f'Дополнительне баллы в {name} даются за:'
        await bot.send_message(callback_query.from_user.id, msg_text)
        for i in spisok:
            await asyncio.sleep(2)
            msg_text = f'{i[0].capitalize()} - вы получите до {i[1]} баллов.'
            await bot.send_message(callback_query.from_user.id, msg_text)
    else:
        await asyncio.sleep(2)
        msg_text = f'Извините, но мы не можем вам ничего посоветовать'
        await bot.send_message(callback_query.from_user.id, msg_text)

@dp.callback_query_handler(text='V20')
async def vz20(callback_query: types.CallbackQuery):
    global skills
    ls = copy.deepcopy(kbs.VUZ20)
    name = ls.pop(0)
    ls.pop(0)
    spisok = []
    flag = 0
    for activity in ls:
        for i in range(5):
            if skills[i] >= activity[2][i]:
                flag += 1
            else:
                flag = 0
        if flag == 5:
            spisok.append(activity[0:2])
        flag = 0

    if len(spisok) != 0:
        msg_text = f'Дополнительне баллы в {name} даются за:'
        await bot.send_message(callback_query.from_user.id, msg_text)
        for i in spisok:
            await asyncio.sleep(2)
            msg_text = f'{i[0].capitalize()} - вы получите до {i[1]} баллов.'
            await bot.send_message(callback_query.from_user.id, msg_text)
    else:
        await asyncio.sleep(2)
        msg_text = f'Извините, но мы не можем вам ничего посоветовать'
        await bot.send_message(callback_query.from_user.id, msg_text)

@dp.callback_query_handler(text='V21')
async def vz21(callback_query: types.CallbackQuery):
    global skills
    ls = copy.deepcopy(kbs.VUZ21)
    name = ls.pop(0)
    ls.pop(0)
    spisok = []
    flag = 0
    for activity in ls:
        for i in range(5):
            if skills[i] >= activity[2][i]:
                flag += 1
            else:
                flag = 0
        if flag == 5:
            spisok.append(activity[0:2])
        flag = 0

    if len(spisok) != 0:
        msg_text = f'Дополнительне баллы в {name} даются за:'
        await bot.send_message(callback_query.from_user.id, msg_text)
        for i in spisok:
            await asyncio.sleep(2)
            msg_text = f'{i[0].capitalize()} - вы получите до {i[1]} баллов.'
            await bot.send_message(callback_query.from_user.id, msg_text)
    else:
        await asyncio.sleep(2)
        msg_text = f'Извините, но мы не можем вам ничего посоветовать'
        await bot.send_message(callback_query.from_user.id, msg_text)

@dp.callback_query_handler(text='V22')
async def vz22(callback_query: types.CallbackQuery):
    global skills
    ls = copy.deepcopy(kbs.VUZ22)
    name = ls.pop(0)
    ls.pop(0)
    spisok = []
    flag = 0
    for activity in ls:
        for i in range(5):
            if skills[i] >= activity[2][i]:
                flag += 1
            else:
                flag = 0
        if flag == 5:
            spisok.append(activity[0:2])
        flag = 0

    if len(spisok) != 0:
        msg_text = f'Дополнительне баллы в {name} даются за:'
        await bot.send_message(callback_query.from_user.id, msg_text)
        for i in spisok:
            await asyncio.sleep(2)
            msg_text = f'{i[0].capitalize()} - вы получите до {i[1]} баллов.'
            await bot.send_message(callback_query.from_user.id, msg_text)
    else:
        await asyncio.sleep(2)
        msg_text = f'Извините, но мы не можем вам ничего посоветовать'
        await bot.send_message(callback_query.from_user.id, msg_text)

@dp.callback_query_handler(text='V23')
async def vz23(callback_query: types.CallbackQuery):
    global skills
    ls = copy.deepcopy(kbs.VUZ23)
    name = ls.pop(0)
    ls.pop(0)
    spisok = []
    flag = 0
    for activity in ls:
        for i in range(5):
            if skills[i] >= activity[2][i]:
                flag += 1
            else:
                flag = 0
        if flag == 5:
            spisok.append(activity[0:2])
        flag = 0

    if len(spisok) != 0:
        msg_text = f'Дополнительне баллы в {name} даются за:'
        await bot.send_message(callback_query.from_user.id, msg_text)
        for i in spisok:
            await asyncio.sleep(2)
            msg_text = f'{i[0].capitalize()} - вы получите до {i[1]} баллов.'
            await bot.send_message(callback_query.from_user.id, msg_text)
    else:
        await asyncio.sleep(2)
        msg_text = f'Извините, но мы не можем вам ничего посоветовать'
        await bot.send_message(callback_query.from_user.id, msg_text)

@dp.callback_query_handler(text='V24')
async def vz24(callback_query: types.CallbackQuery):
    global skills
    ls = copy.deepcopy(kbs.VUZ24)
    name = ls.pop(0)
    ls.pop(0)
    spisok = []
    flag = 0
    for activity in ls:
        for i in range(5):
            if skills[i] >= activity[2][i]:
                flag += 1
            else:
                flag = 0
        if flag == 5:
            spisok.append(activity[0:2])
        flag = 0

    if len(spisok) != 0:
        msg_text = f'Дополнительне баллы в {name} даются за:'
        await bot.send_message(callback_query.from_user.id, msg_text)
        for i in spisok:
            await asyncio.sleep(2)
            msg_text = f'{i[0].capitalize()} - вы получите до {i[1]} баллов.'
            await bot.send_message(callback_query.from_user.id, msg_text)
    else:
        await asyncio.sleep(2)
        msg_text = f'Извините, но мы не можем вам ничего посоветовать'
        await bot.send_message(callback_query.from_user.id, msg_text)

@dp.callback_query_handler(text='V25')
async def vz25(callback_query: types.CallbackQuery):
    global skills
    ls = copy.deepcopy(kbs.VUZ25)
    name = ls.pop(0)
    ls.pop(0)
    spisok = []
    flag = 0
    for activity in ls:
        for i in range(5):
            if skills[i] >= activity[2][i]:
                flag += 1
            else:
                flag = 0
        if flag == 5:
            spisok.append(activity[0:2])
        flag = 0

    if len(spisok) != 0:
        msg_text = f'Дополнительне баллы в {name} даются за:'
        await bot.send_message(callback_query.from_user.id, msg_text)
        for i in spisok:
            await asyncio.sleep(2)
            msg_text = f'{i[0].capitalize()} - вы получите до {i[1]} баллов.'
            await bot.send_message(callback_query.from_user.id, msg_text)
    else:
        await asyncio.sleep(2)
        msg_text = f'Извините, но мы не можем вам ничего посоветовать'
        await bot.send_message(callback_query.from_user.id, msg_text)

@dp.callback_query_handler(text='V26')
async def vz26(callback_query: types.CallbackQuery):
    global skills
    ls = copy.deepcopy(kbs.VUZ26)
    name = ls.pop(0)
    ls.pop(0)
    spisok = []
    flag = 0
    for activity in ls:
        for i in range(5):
            if skills[i] >= activity[2][i]:
                flag += 1
            else:
                flag = 0
        if flag == 5:
            spisok.append(activity[0:2])
        flag = 0

    if len(spisok) != 0:
        msg_text = f'Дополнительне баллы в {name} даются за:'
        await bot.send_message(callback_query.from_user.id, msg_text)
        for i in spisok:
            await asyncio.sleep(2)
            msg_text = f'{i[0].capitalize()} - вы получите до {i[1]} баллов.'
            await bot.send_message(callback_query.from_user.id, msg_text)
    else:
        await asyncio.sleep(2)
        msg_text = f'Извините, но мы не можем вам ничего посоветовать'
        await bot.send_message(callback_query.from_user.id, msg_text)

@dp.callback_query_handler(text='V27')
async def vz27(callback_query: types.CallbackQuery):
    global skills
    ls = copy.deepcopy(kbs.VUZ27)
    name = ls.pop(0)
    ls.pop(0)
    spisok = []
    flag = 0
    for activity in ls:
        for i in range(5):
            if skills[i] >= activity[2][i]:
                flag += 1
            else:
                flag = 0
        if flag == 5:
            spisok.append(activity[0:2])
        flag = 0

    if len(spisok) != 0:
        msg_text = f'Дополнительне баллы в {name} даются за:'
        await bot.send_message(callback_query.from_user.id, msg_text)
        for i in spisok:
            await asyncio.sleep(2)
            msg_text = f'{i[0].capitalize()} - вы получите до {i[1]} баллов.'
            await bot.send_message(callback_query.from_user.id, msg_text)
    else:
        await asyncio.sleep(2)
        msg_text = f'Извините, но мы не можем вам ничего посоветовать'
        await bot.send_message(callback_query.from_user.id, msg_text)

@dp.callback_query_handler(text='V28')
async def vz28(callback_query: types.CallbackQuery):
    global skills
    ls = copy.deepcopy(kbs.VUZ28)
    name = ls.pop(0)
    ls.pop(0)
    spisok = []
    flag = 0
    for activity in ls:
        for i in range(5):
            if skills[i] >= activity[2][i]:
                flag += 1
            else:
                flag = 0
        if flag == 5:
            spisok.append(activity[0:2])
        flag = 0

    if len(spisok) != 0:
        msg_text = f'Дополнительне баллы в {name} даются за:'
        await bot.send_message(callback_query.from_user.id, msg_text)
        for i in spisok:
            await asyncio.sleep(2)
            msg_text = f'{i[0].capitalize()} - вы получите до {i[1]} баллов.'
            await bot.send_message(callback_query.from_user.id, msg_text)
    else:
        await asyncio.sleep(2)
        msg_text = f'Извините, но мы не можем вам ничего посоветовать'
        await bot.send_message(callback_query.from_user.id, msg_text)

@dp.callback_query_handler(text='V29')
async def vz29(callback_query: types.CallbackQuery):
    global skills
    ls = copy.deepcopy(kbs.VUZ29)
    name = ls.pop(0)
    ls.pop(0)
    spisok = []
    flag = 0
    for activity in ls:
        for i in range(5):
            if skills[i] >= activity[2][i]:
                flag += 1
            else:
                flag = 0
        if flag == 5:
            spisok.append(activity[0:2])
        flag = 0

    if len(spisok) != 0:
        msg_text = f'Дополнительне баллы в {name} даются за:'
        await bot.send_message(callback_query.from_user.id, msg_text)
        for i in spisok:
            await asyncio.sleep(2)
            msg_text = f'{i[0].capitalize()} - вы получите до {i[1]} баллов.'
            await bot.send_message(callback_query.from_user.id, msg_text)
    else:
        await asyncio.sleep(2)
        msg_text = f'Извините, но мы не можем вам ничего посоветовать'
        await bot.send_message(callback_query.from_user.id, msg_text)

@dp.callback_query_handler(text='V30')
async def vz30(callback_query: types.CallbackQuery):
    global skills
    ls = copy.deepcopy(kbs.VUZ30)
    name = ls.pop(0)
    ls.pop(0)
    spisok = []
    flag = 0
    for activity in ls:
        for i in range(5):
            if skills[i] >= activity[2][i]:
                flag += 1
            else:
                flag = 0
        if flag == 5:
            spisok.append(activity[0:2])
        flag = 0

    if len(spisok) != 0:
        msg_text = f'Дополнительне баллы в {name} даются за:'
        await bot.send_message(callback_query.from_user.id, msg_text)
        for i in spisok:
            await asyncio.sleep(2)
            msg_text = f'{i[0].capitalize()} - вы получите до {i[1]} баллов.'
            await bot.send_message(callback_query.from_user.id, msg_text)
    else:
        await asyncio.sleep(2)
        msg_text = f'Извините, но мы не можем вам ничего посоветовать'
        await bot.send_message(callback_query.from_user.id, msg_text)


if __name__ == "__main__":
    # Запуск бота
    executor.start_polling(dp, skip_updates=True)