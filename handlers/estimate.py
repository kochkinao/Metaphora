from aiogram import types, Dispatcher
from state import UserState
import kb

async def back_last(msg:types.Message):
    await UserState.estination.set()
    await msg.answer('Оцените бота', reply_markup=kb.estination)

async def estin(msg:types.Message):
    await UserState.last.set()
    await msg.answer('Благодарю тебя за использование бота и за оценку! Приглашаю тебя на мой канал, если ты еще не подписан(а), там много полезной информации по работе с МАК-картами и пониманию себя и своих истинных желаний. Также ты можешь записаться ко мне на коуч-сессию и консультацию с МАК-картами.',
                     reply_markup=kb.last)

def register_handler_estimate(dp:Dispatcher):
    dp.register_message_handler(back_last, text='Оценить', state=UserState.answer)
    dp.register_message_handler(estin, state=UserState.estination, text=[f'Отлично {kb.top}', f'Нормально {kb.medium}', f'Плохо {kb.bad}'])

