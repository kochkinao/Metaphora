import kb, random, os
from state import UserState
from aiogram import types, Dispatcher
from create_bot import bot
import photo, time

async def random_deck(msg:types.Message):
    with open('./img/Radost/' + random.choice(os.listdir('./img/Radost/')), 'rb') as ph_radost:
        await bot.send_photo(msg.from_user.id, photo=ph_radost)
    time.sleep(3)
    with open(photo.video, 'rb') as video:
        await bot.send_video(msg.from_user.id, video=video, caption='Видео с уточнениями по работе с МАК-картами для тебя')
    time.sleep(5)
    await msg.answer('Если тебе интересно, как работать с МАК-картами самостоятельно для разрешения своих запросов, то я рекомендую прочитать мою бесплатную инструкцию.', reply_markup=kb.tg)
    time.sleep(1)
    await UserState.estination.set()
    await msg.answer('Оцени этот раздел', reply_markup=kb.estination)

def register_handler_deck_day(dp:Dispatcher):
    dp.register_message_handler(random_deck, state=UserState.kart_day, text='Вытянуть карту')

