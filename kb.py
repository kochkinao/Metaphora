import emoji
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton

import config

#REPLY MAIN MENU
nachat_razbor = KeyboardButton(text='Начать разбор')
MAK = KeyboardButton(text='Что такое МАК карты?')
day = KeyboardButton (text='Карта дня')
start = ReplyKeyboardMarkup(resize_keyboard=True).add(nachat_razbor).row(MAK, day)

# REPLY Buttons "Back" and "Main menu"
back = KeyboardButton(text = 'Назад')
main_menu = KeyboardButton(text = 'Главное меню')
main_menu_kb = ReplyKeyboardMarkup(resize_keyboard=True).add(main_menu)

#REPLY THEMS
phinans = KeyboardButton (text='Финансы')
otnoshenia = KeyboardButton (text='Отношения')
zdorovie = KeyboardButton (text='Здоровье')
realizacia = KeyboardButton (text='Реализация')
sostoyanie = KeyboardButton(text='Состояние')
thems = ReplyKeyboardMarkup(resize_keyboard=True).row(phinans, otnoshenia).row(zdorovie, realizacia).add(sostoyanie).add(back)

#REPLY DECKS
allegorii = KeyboardButton (text='Аллегории')
radost = KeyboardButton (text='Радости внутреннего ребенка')
strah = KeyboardButton (text='Внутренние страхи')
decks = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).row(allegorii, radost).row(strah).add(back, main_menu)

#REPLY NUMS
one = KeyboardButton(text='1')
two = KeyboardButton(text='2')
three = KeyboardButton(text='3')
four = KeyboardButton(text='4')
five = KeyboardButton(text='5')
six = KeyboardButton(text='6')
num = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).row(one,two,three).row(four,five,six).add(back, main_menu)

#REPLY "Don't want"
ne_hochy = KeyboardButton(text = 'Не хочу отправлять')
zhelanie = ReplyKeyboardMarkup(resize_keyboard=True).add(ne_hochy)

#REPLY "Yes" and "No"
yes = KeyboardButton(text='Да')
no = KeyboardButton(text='Нет')
yes_no = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(yes, no).add(main_menu)

#REPLY "Estimate" and "Try again"
ozenka = KeyboardButton(text = 'Оценить')
ocenka = ReplyKeyboardMarkup(resize_keyboard=True).add(ozenka).add(main_menu)

#REPLY ESTIMATE SMIL
smile1 = KeyboardButton(text=f'Отлично 😃')
smile2 = KeyboardButton(text=f'Нормально 😌')
smile3 = KeyboardButton(text=f'Плохо 😠')
estination = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(smile3, smile2, smile1).add(main_menu)

#REPLY PULL OUT A CARD
pull = KeyboardButton(text='Вытянуть карту')
pull_out = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(pull)


#INLINE PRODOLZHIT S BOTOM
cont_with_bot = InlineKeyboardButton(text = 'Продолжить самостоятельно', callback_data='С ботом1')
s_botom1 = InlineKeyboardMarkup().add(cont_with_bot)

cont_with_bot = InlineKeyboardButton(text = 'Продолжить самостоятельно', callback_data='С ботом2')
s_botom2 = InlineKeyboardMarkup().add(cont_with_bot)

# INLINE INSTRUCTION
btn_tg = InlineKeyboardButton(text='Получить инструкцию БЕСПЛАТНО', url=config.LINK, callback_data='канал2')
tg = InlineKeyboardMarkup().add(btn_tg)

# INLINE LAST BUTTON
chanel_in = InlineKeyboardButton(text='Перейти в канал', url=config.LINK, callback_data='канал1')
main_menu_in = InlineKeyboardMarkup(text='Главное меню', callback_data='main_menu_last')
last = InlineKeyboardMarkup().add(chanel_in).add(main_menu_in)

# REPLY ADMIN PANEL
stat = KeyboardButton(text='Статистика')
m_panel = ReplyKeyboardMarkup(resize_keyboard=True).add(stat).add(main_menu)
all_users = KeyboardButton(text='Всего пользователей')
estimate = KeyboardButton(text='Оценка')
usage = KeyboardButton(text='Использований')
unik = KeyboardButton(text='Уникальных')
new = KeyboardButton(text='Новых')
regular = KeyboardButton(text='Регулярных')
go_to_chanel = KeyboardButton(text='Переходов в канал')
all_stat = KeyboardButton(text='Общая статистика')
s_panel = ReplyKeyboardMarkup(resize_keyboard=True).row(all_users, estimate, usage).row(unik, new, regular).row(all_stat, back, go_to_chanel)
