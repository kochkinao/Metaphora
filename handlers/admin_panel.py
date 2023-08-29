from aiogram import types, Dispatcher

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
    a = bd.getting_the_nuber_of_users(0)
    await msg.answer(f'Всего пользователей <b>{a}</b>', parse_mode="HTML")


async def usage(msg: types.Message):
    await msg.answer(
        f'<i>Основная</i> ветка была пройдена:\n<b>?</b> раз за день\n<b>?</b> раз за неделю\n<b>?</b> раз за месяц',
        parse_mode='HTML')
    await msg.answer(
        f'Ветка <i>"Карта дня"</i> была пройдена:\n<b>?</b> раз за день\n<b>?</b> раз за неделю\n<b>?</b> раз за месяц',
        parse_mode='HTML')


async def unik(msg: types.Message):
    await msg.answer(f'<i>Основную</i> ветку посетили за сегодня <b>?</b> раз', parse_mode='HTML')
    await msg.answer(f'Ветку <i>"Карта дня"</i> посетили за сегодня <b>?</b> раз', parse_mode='HTML')


async def new(msg: types.Message):
    await msg.answer(f'Новых пользователей:\n<b>?</b> за день\n<b>?</b> за неделю\n<b>?</b> за месяц',
                     parse_mode='HTML')


async def regular(msg: types.Message):
    await msg.answer(f'Регулярных пользователей <b>?</b>', parse_mode='HTML')


async def go_channel(msg: types.Message):
    await msg.answer(f'Переходов в канал <b>?</b>', parse_mode='HTML')


async def back(msg: types.Message):
    await msg.answer('Возвращаюсь', reply_markup=kb.m_panel)
    await UserState.admin_stat.set()


async def all_stat(msg: types.Message):
    await msg.answer(f'Всего пользователей <b>{a}</b>\n\n'
                     f'<i>Основная</i> ветка была пройдена:\n<b>?</b> раз за день\n<b>?</b> раз за неделю\n<b>?</b> раз за месяц\n'
                     f'Ветка <i>"Карта дня"</i> была пройдена:\n<b>?</b> раз за день\n<b>?</b> раз за неделю\n<b>?</b> раз за месяц\n\n'
                     f'<i>Основную</i> ветку посетили за сегодня <b>?</b> раз\n'
                     f'Ветку <i>"Карта дня"</i> посетили за сегодня <b>?</b> раз\n\n'
                     f'Новых пользователей:\n<b>?</b> за день\n<b>?</b> за неделю\n<b>?</b> за месяц\n\n'
                     f'Регулярных пользователей <b>?</b>\n\n'
                     f'Переходов в канал <b>?</b>', parse_mode='HTML')

def register_handler_admin_panel(dp: Dispatcher):
    dp.register_message_handler(admin, state='*', commands=['admin'])
    dp.register_message_handler(admin_panel, state=UserState.password, text='Кот в зимних сапогах')
    dp.register_message_handler(stat, state=UserState.admin_stat, text='Статистика')
    dp.register_message_handler(all_users, state=UserState.select_stat, text='Всего пользователей')
    dp.register_message_handler(usage, state=UserState.select_stat, text='Использований')
    dp.register_message_handler(unik, state=UserState.select_stat, text='Уникальных')
    dp.register_message_handler(new, state=UserState.select_stat, text='Новых')
    dp.register_message_handler(regular, state=UserState.select_stat, text='Регулярных')
    dp.register_message_handler(go_channel, state=UserState.select_stat, text='Переходов в канал')
    dp.register_message_handler(back, state=UserState.select_stat, text='Назад')
    dp.register_message_handler(all_stat, state=UserState.select_stat, text='Общая статистика')
