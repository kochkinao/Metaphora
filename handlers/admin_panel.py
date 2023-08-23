from aiogram import types, Dispatcher
import bd
import kb
from state import UserState

async def admin(msg:types.Message):
    await msg.answer('Введите админ-пароль:')

async def admin_panel(msg:types.Message):
    await msg.answer('Приветствую, администратор 👾\nВыберите, что Вы хотите сделать', reply_markup=kb.statistic)
    await UserState.admin_stat.set()

async def stat(msg:types.Message):
    a = bd.getting_the_nuber_of_users(0)
    await msg.answer(f'Всего пользователей <b>{a}</b>', parse_mode="HTML")

def register_handler_admin_panel(dp: Dispatcher):
    dp.register_message_handler(admin, state='*', commands=['admin'])
    dp.register_message_handler(admin_panel, state='*', text='Кот в зимних сапогах')
    dp.register_message_handler(stat, state=UserState.admin_stat, text='Статистика')
