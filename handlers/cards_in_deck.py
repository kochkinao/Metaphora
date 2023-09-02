from aiogram import types, Dispatcher

import kb
import os
import random
import time
from create_bot import bot
from state import UserState


async def pic1(msg:types.Message):
    await UserState.questi.set()
    with open('./img/Allegorii/' + random.choice(os.listdir('./img/Allegorii/')), 'rb') as ph_al:
        await bot.send_photo(msg.from_user.id, photo=ph_al)
    await msg.answer(
        'На этом этапе важно верно проанализировать, как эта карта отвечает на твой вопрос. Для этого нужно сконцентрироваться на своих ассоциациях. В моей инструкции я собрала ряд вопросов, которые тебе могут помочь',
        reply_markup=kb.tg)
    time.sleep(5)
    await msg.answer('Ты можешь продолжить разбор самостоятельно, нажав на кнопку ниже',
                     reply_markup=kb.s_botom2)

async def pic2(msg: types.Message):
    await UserState.questi.set()
    with open('./img/Radost/' + random.choice(os.listdir('./img/Radost/')), 'rb') as ph_radost:
        await bot.send_photo(msg.from_user.id, photo=ph_radost)
    await msg.answer(
        'На этом этапе важно верно проанализировать, как эта карта отвечает на твой вопрос. Для этого нужно сконцентрироваться на своих ассоциациях. В моей инструкции я собрала ряд вопросов, которые тебе могут помочь',
        reply_markup=kb.tg)
    time.sleep(5)
    await msg.answer('Ты можешь продолжить разбор самостоятельно, нажав на кнопку ниже',
                     reply_markup=kb.s_botom2)

async def pic3(msg: types.Message):
    await UserState.questi.set()
    with open('./img/Strah/' + random.choice(os.listdir('./img/Strah/')), 'rb') as ph_strah:
        await bot.send_photo(msg.from_user.id, photo=ph_strah)
    await msg.answer(
        'На этом этапе важно верно проанализировать, как эта карта отвечает на твой вопрос. Для этого нужно сконцентрироваться на своих ассоциациях. В моей инструкции я собрала ряд вопросов, которые тебе могут помочь',
        reply_markup=kb.tg)
    time.sleep(5)
    await msg.answer('Ты можешь продолжить разбор самостоятельно, нажав на кнопку ниже',
                     reply_markup=kb.s_botom2)

def register_handler_cards_in_deck(dp:Dispatcher):
    dp.register_message_handler(pic1, state=UserState.allegorii3, text=['1', '2', '3', '4', '5', '6'])
    dp.register_message_handler(pic2, state=UserState.radost3, text=['1', '2', '3', '4', '5', '6'])
    dp.register_message_handler(pic3, state=UserState.strah3, text=['1', '2', '3', '4', '5', '6'])

