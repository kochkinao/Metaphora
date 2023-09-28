from aiogram import types, Dispatcher
from create_bot import db
from aiogram.dispatcher import FSMContext
import kb
from state import UserState
from create_bot import bot

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

async def start(msg: types.Message):
    await msg.answer(f'Всего нажатий start <b>{db.get_start_user()}</b>', parse_mode='HTML')

async def estim(msg:types.Message):
    await msg.answer(f'Учавствующие в опросе ответили:\n<i>Отлично</i> <b>{db.get_good()}</b> раз(а)\n<i>Нормально</i> <b>{db.get_normal()}</b> раз(а)\n<i>Плохо</i> <b>{db.get_bad()}</b> раз(а)',
                     parse_mode='HTML')

async def back(msg: types.Message):
    await msg.answer('Возвращаюсь', reply_markup=kb.m_panel)
    await UserState.admin_stat.set()

async def newsletter_check(msg: types.Message):
    await msg.answer('Введите сообщение, которое хотите отправить пользователям', reply_markup=kb.back)
    await UserState.newsletter1.set()

async def newsletter_text(msg: types.Message, state: FSMContext):
    users = db.get_user()
    await state.update_data(text=msg.text)
    a = await state.get_data()
    text = a['text']
    for row in users:
        try:
            await bot.send_message(row[0], text = text)
        except:
            pass
    await msg.answer('Рассылка отправлена')

async def newsletter_photo(msg: types.Message, state: FSMContext):
    users = db.get_user()
    await state.update_data(photo_id=msg.photo[0].file_id)
    await state.update_data(caption=msg.caption)
    a = await state.get_data()
    photo_id = a['photo_id']
    caption = a['caption']
    for row in users:
        try:
            await bot.send_photo(row[0], photo = photo_id, caption=caption)
        except:
            pass
    await msg.answer('Рассылка отправлена')

async def newsletter_video(msg: types.Message, state: FSMContext):
    users = db.get_user()
    await state.update_data(video_id=msg.video.file_id)
    await state.update_data(caption=msg.caption)
    a = await state.get_data()
    video_id = a['video_id']
    caption = a['caption']
    for row in users:
        try:
            await bot.send_video(row[0], video = video_id, caption=caption)
        except:
            pass
    await msg.answer('Рассылка отправлена')

async def newsletter_note(msg: types.Message, state: FSMContext):
    users = db.get_user()
    await state.update_data(note_id=msg.video_note.file_id)
    a = await state.get_data()
    note_id = a['note_id']
    for row in users:
        try:
            await bot.send_video_note(row[0], video_note=note_id)
        except:
            pass
    await msg.answer('Рассылка отправлена')

async def newsletter_document(msg: types.Message, state: FSMContext):
    users = db.get_user()
    await state.update_data(document_id=msg.document.file_id)
    await state.update_data(caption=msg.caption)
    a = await state.get_data()
    document_id = a['document_id']
    caption = a['caption']
    for row in users:
        try:
            await bot.send_document(row[0], document=document_id, caption=caption)
        except:
            pass
    await msg.answer('Рассылка отправлена')

async def newsletter_voice(msg: types.Message, state: FSMContext):
    users = db.get_user()
    await state.update_data(voice_id=msg.voice.file_id)
    a = await state.get_data()
    voice_id = a['voice_id']
    for row in users:
        try:
            await bot.send_voice(row[0], voice = voice_id)
        except:
            pass
    await msg.answer('Рассылка отправлена')


def register_handler_admin_panel(dp: Dispatcher):
    dp.register_message_handler(admin, state='*', commands=['admin'])
    dp.register_message_handler(admin_panel, state=UserState.password, text='Кот в зимних сапогах')
    dp.register_message_handler(stat, state=UserState.admin_stat, text='Статистика')
    dp.register_message_handler(all_users, state=UserState.select_stat, text='Всего пользователей')
    dp.register_message_handler(estim, state=UserState.select_stat, text = 'Оценка')
    dp.register_message_handler(back, state=[UserState.select_stat, UserState.newsletter1], text='Назад')
    dp.register_message_handler(start, state=UserState.select_stat, text = 'Кол-во нажатий start')
    dp.register_message_handler(newsletter_check, state=UserState.admin_stat, text = 'Рассылка сообщения')
    dp.register_message_handler(newsletter_text, state=UserState.newsletter1)
    dp.register_message_handler(newsletter_photo, state=UserState.newsletter1, content_types='photo')
    dp.register_message_handler(newsletter_note, state=UserState.newsletter1, content_types='video_note')
    dp.register_message_handler(newsletter_document, state=UserState.newsletter1, content_types='document')
    dp.register_message_handler(newsletter_voice, state=UserState.newsletter1, content_types='voice')
    dp.register_message_handler(newsletter_video, state=UserState.newsletter1, content_types='video')
