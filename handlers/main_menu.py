from aiogram import types, Dispatcher
from state import UserState
from aiogram.dispatcher import FSMContext
from bd import set_chat_id
from config import LINK
import kb

async def hi(msg:types.Message, state: FSMContext):
    set_chat_id(msg.from_user.id)
    await state.finish()
    await UserState.start_menu.set() #select in main menu
    await msg.answer(f"Привет, рада тебя здесь видеть. Этот бот поможет тебе разрешить запрос из разных сфер жизни, а также посмотреть полезные рекомендации. Создатель бота – Я, Ксения Барашкина, Лайф-Коуч и МАК-терапевт. Моя главная задача - это облегчать жизнь людям и улучшать их состояние. Буду рада видеть тебя на своем <a href='{LINK}'>канале.</a>",
                     reply_markup=kb.start, parse_mode="HTML")

async def start_razbor(msg:types.Message):
    await UserState.thems.set() #select thems
    await msg.answer('Выбери тему',
                     reply_markup=kb.thems)

async def mak_karty(msg:types.Message):
    await msg.answer("Метафорические ассоциативные карты — это психологический инструмент для обращения к подсознанию через ассоциации.\n\nЭто не тот вариант, когда мы раскладываем карты и получаем готовый ответ извне. Метафорические карты не имеют однозначной интерпретации. Когда мы смотрим на карту, мы описываем ассоциации, которые возникают в нас самих и имеют отношение только к нам.\n\nАссоциативные карты позволяют заглянуть в себя и найти ответы на интересующие вопросы — они помогают услышать свое подсознание, в котором скрыты наши истинные желания, мотивы, потребности.",
                     reply_markup=kb.start)

async def karta_dnya(msg:types.Message):
    await UserState.kart_day.set()
    await msg.answer('Простой и интересный вариант для быстрого самоисследования с одной картой. Сосредоточься на актуальном вопросе, который важен для тебя сегодня. Вытяни карту и проанализируй, какие ассоциации она вызывает')
    await msg.answer(f'Пример:\n<i>На что мне сегодня важно обратить внимание?\nНа какой теме важно сейчас сосредоточиться?\nКак я себя чувствую сейчас?</i>',
                     reply_markup=kb.pull_out,
                     parse_mode='HTML')

def register_handler_main_menu(dp:Dispatcher):
    dp.register_message_handler(hi, commands=['start', 'restart'], state='*')
    dp.register_message_handler(start_razbor, text='Начать разбор', state=UserState.start_menu)
    dp.register_message_handler(mak_karty, text='Что такое МАК карты?', state=UserState.start_menu)
    dp.register_message_handler(karta_dnya, text='Карта дня', state=UserState.start_menu)