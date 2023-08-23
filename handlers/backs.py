from aiogram import types, Dispatcher
from state import UserState
import kb

async def back(msg:types.Message):
    await UserState.start_menu.set()
    await msg.answer('Возвращаюсь назад', reply_markup=kb.start)

async def back2(msg:types.Message):
    await UserState.thems.set()
    await msg.answer('Возвращаюсь назад', reply_markup=kb.thems)

async def main_menu(msg:types.Message,):
    await UserState.start_menu.set()
    await msg.answer('Возвращаюсь в главное меню', reply_markup=kb.start)

async def main_menu_last(callback:types.CallbackQuery):
    await UserState.start_menu.set()
    await callback.message.answer('Возвращаюсь в главное меню', reply_markup=kb.start)

async def back_kolody(msg:types.Message):
    await UserState.select_deck.set()
    await msg.answer('Возвращаюсь', reply_markup=kb.decks)

def regiser_handler_backs(dp: Dispatcher):
    dp.register_message_handler(back, text='Назад', state = UserState.thems)
    dp.register_message_handler(back2, text='Назад', state = UserState.select_deck)
    dp.register_message_handler(main_menu, text='Главное меню', state = '*')
    dp.register_callback_query_handler(main_menu_last, text='main_menu_last', state=UserState.last)
    dp.register_message_handler(back_kolody, text='Назад', state=[UserState.allegorii3, UserState.radost3, UserState.strah3])