from aiogram import types, Dispatcher
from state import UserState
from aiogram.dispatcher import FSMContext
import kb

async def s_botom_handler(callback: types.CallbackQuery):
    await callback.message.answer('Как эта карта отвечает на твой вопрос?\n\nДля более глубоко понимания и анализа отправь ответ в чат. Этот чат конфиденциальный, никто (включая меня) не увидит твои ответы',
                                  reply_markup=kb.zhelanie)
    await UserState.question1.set()

async def reply(msg:types.message, state:FSMContext):
    await state.update_data(question1 = msg.text)
    await msg.answer('Что ты видишь на карте?',
                     reply_markup=kb.zhelanie)
    await UserState.question2.set()

async def reply2(msg:types.message, state:FSMContext):
    await state.update_data(question2 = msg.text)
    await msg.answer('Опиши подробно кто и что на ней изображены? Какая ситуация проигрывается на картинке?',
                     reply_markup=kb.zhelanie)
    await UserState.question3.set()

async def reply3(msg:types.message, state:FSMContext):
    await state.update_data(question3 = msg.text)
    await msg.answer('Что, на твой взгляд, чувствуют и переживают персонаж(и)?',
                     reply_markup=kb.zhelanie)
    await UserState.question4.set()

async def reply4(msg:types.message, state:FSMContext):
    await state.update_data(question4 = msg.text)
    await msg.answer('Ты есть на этой карте? Если есть, то где? Если нет, то какова твоя роль в этой композиции?',
                     reply_markup=kb.zhelanie)
    await UserState.question5.set()

async def reply5(msg:types.message, state:FSMContext):
    await state.update_data(question5 = msg.text)
    await msg.answer('Что ты чувствуешь, смотря на это изображение? Что тебе хочется сделать, смотря на карту?',
                     reply_markup=kb.zhelanie)
    await UserState.question6.set()

async def reply6(msg:types.message, state:FSMContext):
    await state.update_data(question6 = msg.text)
    await msg.answer('Как эта карта отвечает на твой основной вопрос?',
                     reply_markup=kb.zhelanie)
    await UserState.question7.set()

def register_handler_help_with_card_description(dp:Dispatcher):
    dp.register_callback_query_handler(s_botom_handler, text='С ботом2', state=UserState.questi)
    dp.register_message_handler(reply, state = UserState.question1)
    dp.register_message_handler(reply2, state=UserState.question2)
    dp.register_message_handler(reply3, state=UserState.question3)
    dp.register_message_handler(reply4, state=UserState.question4)
    dp.register_message_handler(reply5, state=UserState.question5)
    dp.register_message_handler(reply6, state=UserState.question6)