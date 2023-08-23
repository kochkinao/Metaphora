from state import UserState
from aiogram import types, Dispatcher
from create_bot import bot
import kb, photo, time

async def main_line(msg: types.Message):
    global them
    them = msg.text
    await UserState.select_deck.set()
    await msg.answer('Выберите колоду', reply_markup=kb.decks)
    await msg.answer('· Колода "Радости внутреннего ребенка" помогает услышать истинные желания\n\n· Колода «Внутренние страхи» помогает понять, что тебе мешает, тормозит или ограничивает в достижении целей\n\n·	Колода «Аллегории» - универсальная колода')

async def answer_yes_no(msg:types.Message):
    await UserState.estination.set()
    if msg.text == 'Да':
        await msg.answer('Я рада, что бот помог ответить на волнующий вопрос!\nЯ подготовила для тебя видео по теме твоего запроса')
        if them == 'Финансы':
            with open(photo.video, 'rb') as video:
                await bot.send_video(msg.from_user.id, video=video)
            time.sleep(5)
            await msg.answer('Пожалуйста, оцените бота. Это нужно для его улучшения', reply_markup=kb.estination)
        elif them == 'Отношения':
            with open(photo.video, 'rb') as video:
                await bot.send_video(msg.from_user.id, video=video)
            time.sleep(5)
            await msg.answer('Пожалуйста, оцените бота. Это нужно для его улучшения', reply_markup=kb.estination)
        elif them == 'Здоровье':
            with open(photo.video, 'rb') as video:
                await bot.send_video(msg.from_user.id, video=video)
            time.sleep(5)
            await msg.answer('Пожалуйста, оцените бота. Это нужно для его улучшения', reply_markup=kb.estination)
        elif them == 'Реализация':
            with open(photo.video, 'rb') as video:
                await bot.send_video(msg.from_user.id, video=video)
            time.sleep(5)
            await msg.answer('Пожалуйста, оцените бота. Это нужно для его улучшения', reply_markup=kb.estination)
        elif them == 'Состояние':
            with open(photo.video, 'rb') as video:
                await bot.send_video(msg.from_user.id, video=video)
            time.sleep(5)
            await msg.answer('Пожалуйста, оцените бота. Это нужно для его улучшения', reply_markup=kb.estination)

    elif msg.text == 'Нет':
        await msg.answer('Сожалею, что бот не помог разобраться с волнующим запросом. Такое бывает, возможно, тебе стоит поразмыслить над самим запросом, действительно ли он главный для тебя сейчас? Если ты чувствуешь трудности с формулировкой запроса или трактовкой карты, то приглашаю тебя на консультацию, на которой мы подробно разберем твою ситуацию.',
                         reply_markup=kb.ocenka)
        time.sleep(2)
        await msg.answer('Пожалуйста, оцените бота. Это нужно для его улучшения', reply_markup=kb.estination)

def register_handler_thems_and_answer_your_question(dp:Dispatcher):
    dp.register_message_handler(answer_yes_no, state = UserState.question8, text = ['Да', 'Нет'])
    dp.register_message_handler(main_line, text=['Финансы', 'Отношения', 'Здоровье', 'Реализация', 'Состояние'], state=UserState.thems)