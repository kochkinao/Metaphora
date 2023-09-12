from aiogram import types, Dispatcher
from state import UserState
from create_bot import db
import kb

async def back_last(msg:types.Message):
    await UserState.estination.set()
    await msg.answer('Оцените бота', reply_markup=kb.estination)

async def estin(msg:types.Message):
    await UserState.last.set()
    if msg.text == 'Отлично 😃':
        db.add_good()
    elif msg.text == 'Нормально 😌':
        db.add_normal()
    elif msg.text == 'Плохо 😠':
        db.add_bad()
    await msg.answer('Благодарю тебя за использование бота и за оценку! Приглашаю тебя на мой канал, если ты еще не подписан(а), там много полезной информации по работе с МАК-картами и пониманию себя и своих истинных желаний. Также ты можешь записаться ко мне на коуч-сессию и консультацию с МАК-картами.\n\nВидео про МАК-карты на YouTube можно посмотреть по ссылке: https://youtu.be/fz2lIa6G49Y?si=S8S0o--XnjKm6eAj',
                     reply_markup=kb.last)

def register_handler_estimate(dp:Dispatcher):
    dp.register_message_handler(back_last, text='Оценить', state=UserState.answer)
    dp.register_message_handler(estin, state=UserState.estination, text=[f'Отлично 😃', f'Нормально 😌', f'Плохо 😠'])

