from aiogram import types, Dispatcher
from create_bot import db

import bd
import kb
from state import UserState

async def admin(msg: types.Message):
    await msg.answer('Введите админ-пароль:')
    await UserState.password.set()

async def admin_panel(msg: types.Message):
    await msg.answer('Приветствую, администратор 👾\nВыберите, что Вы хотите сделать', reply_markup=kb.m_panel)
    await UserState.admin_stat.set()

async def stat(msg: types.Message):
    await msg.answer('Выберите пункт, статистику которого Вы хотите получить', reply_markup=kb.s_panel)
    await UserState.select_stat.set()

async def all_users(msg: types.Message):
    await msg.answer(f'Всего пользователей <b>{db.all_users()}</b>', parse_mode="HTML")

async def estim(msg:types.Message):
    await msg.answer(f'Учавствующие в опросе ответили:\n<i>Отлично</i> <b>{db.get_good()}</b> раз(а)\n<i>Нормально</i> <b>{db.get_normal()}</b> раз(а)\n<i>Плохо</i> <b>{db.get_bad()}</b> раз(а)',
                     parse_mode='HTML')

async def back(msg: types.Message):
    await msg.answer('Возвращаюсь', reply_markup=kb.m_panel)
    await UserState.admin_stat.set()

def register_handler_admin_panel(dp: Dispatcher):
    dp.register_message_handler(admin, state='*', commands=['admin'])
    dp.register_message_handler(admin_panel, state=UserState.password, text='Кот в зимних сапогах')
    dp.register_message_handler(stat, state=UserState.admin_stat, text='Статистика')
    dp.register_message_handler(all_users, state=UserState.select_stat, text='Всего пользователей')
    dp.register_message_handler(estim, state=UserState.select_stat, text = 'Оценка')
    dp.register_message_handler(back, state=UserState.select_stat, text='Назад')
