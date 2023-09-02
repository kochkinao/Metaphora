from aiogram import types, Dispatcher
from state import UserState
from aiogram.dispatcher import FSMContext
from create_bot import bot
import kb, photo

async def select_card1(msg: types.Message):
    await UserState.allegorii3.set()
    global mes
    mes = msg.text
    with open(photo.ryb_al, 'rb') as ryb_al:
        await bot.send_photo(msg.from_user.id, caption='Выбери карту из колоды', photo=ryb_al, reply_markup=kb.num)

async def select_card2(msg: types.Message):
    await UserState.radost3.set()
    global mes
    mes = msg.text
    with open(photo.ryb_radost, 'rb') as ryb_radost:
        await bot.send_photo(msg.from_user.id, caption='Выбери карту из колоды', photo=ryb_radost, reply_markup=kb.num)

async def select_card3(msg: types.Message):
    await UserState.strah3.set()
    global mes
    mes = msg.text
    with open(photo.ryb_strah, 'rb') as ryb_strah:
        await bot.send_photo(msg.from_user.id, caption='Выбери карту из колоды', photo=ryb_strah, reply_markup=kb.num)

async def last_answer(msg:types.message, state:FSMContext):
    await state.update_data(question6 = msg.text)
    if mes == 'Не хочу отправлять':
        await msg.answer(f'Ты смог(-ла) ответить на свой вопрос?', reply_markup=kb.yes_no)
        await UserState.question7.set()
    else:
        await msg.answer(f'Ты смог(-ла) ответить на свой вопрос?\nВопрос: "<i>{mes}</i>"', parse_mode = "HTML", reply_markup=kb.yes_no)
        await UserState.question7.set()

def register_handler_where_are_you_able_to_answer(dp: Dispatcher):
    dp.register_message_handler(select_card1, state=UserState.allegorii2)
    dp.register_message_handler(select_card2, state=UserState.radost2)
    dp.register_message_handler(select_card3, state=UserState.strah2)
    dp.register_message_handler(last_answer, state=UserState.question6)